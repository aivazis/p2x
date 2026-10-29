#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a plain attribute in a class that is not a configurable hides an inherited trait, under
its name and its aliases, when it comes first in the derivation
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# a lookup that should fail
def missing(configurable: type, alias: str) -> bool:
    """
    Check that {configurable} has no trait that answers to {alias}
    """
    # attempt to
    try:
        # look up the trait
        configurable._p2x_trait(alias)
    # if nobody recognizes {alias}
    except p2x.exceptions.TraitNotFoundError as error:
        # make sure the error says who and what
        return error.configurable is configurable and error.alias == alias
    # if the lookup succeeded, it's not missing
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

    # python finds the plain attribute
    assert TrackSaw.kerf == 0.125
    # so the trait is hidden under its name
    assert missing(TrackSaw, "kerf")
    # and its alias
    assert missing(TrackSaw, "cut-width")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
