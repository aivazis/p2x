#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable with two parents that share an ancestor reads the default of the trait
python finds, even when the redeclaration comes from the parent listed second
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
    Derive a configurable from two saws that share an ancestor, only the second of which
    redeclares a trait
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # with a preferred value
        kerf.default = 0.125
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # a saw that runs along a rail
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # the length of the rail
        rail = p2x.traits.properties.float()
        # with a preferred value
        rail.default = 55.0

    # a saw with a blade of its own
    class FineSaw(PanelSaw):
        """
        A panel saw with a thinner blade
        """

        # the width of its cut, with no other names
        kerf = p2x.traits.properties.float()
        # and a preferred value of its own
        kerf.default = 0.0625

    # a saw that is both
    class RailSaw(TrackSaw, FineSaw):
        """
        A fine saw that runs along a rail
        """

    # python puts the second parent ahead of the shared ancestor
    assert RailSaw.__mro__.index(FineSaw) < RailSaw.__mro__.index(PanelSaw)
    # so, under the name, the saw reads the default of the redeclared trait
    assert RailSaw.kerf == 0.0625
    # the alias went with the trait it replaced, so it reads nothing
    assert missing(RailSaw, "cut-width")
    # and the trait of the first parent gives its own default
    assert RailSaw.rail == 55.0

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
