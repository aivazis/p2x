#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that, when a plain class comes first in the derivation, a configurable reads its attribute
under the name of the trait it hides, and nothing under the aliases of that trait
"""

# support
import p2x.components
import p2x.traits.properties


# a read that should fail
def missing(configurable: type, alias: str) -> bool:
    """
    Check that reading {alias} through {configurable} finds nothing
    """
    # attempt to
    try:
        # read it
        getattr(configurable, alias)
    # if nothing answers to {alias}
    except AttributeError as error:
        # make sure the error says who and what, and that asking agrees
        return (
            error.obj is configurable and error.name == alias and not hasattr(configurable, alias)
        )
    # if the read succeeded, it's not missing
    return False


# the test
def test() -> None:
    """
    Derive a configurable from a plain class and a configurable, in that order
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # with a preferred value
        kerf.default = 0.25
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # a plain class with a fixed kerf
    class Fixed:
        """
        A blade that always cuts the same width
        """

        # the width of its cut
        kerf = 0.125

    # a saw with the fixed blade listed first
    class TrackSaw(Fixed, PanelSaw):
        """
        A panel saw with a fixed blade
        """

    # under the name, the saw reads the plain attribute of the blade
    assert TrackSaw.kerf == 0.125
    # and under the alias of the hidden trait, it reads nothing
    assert missing(TrackSaw, "cut-width")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
