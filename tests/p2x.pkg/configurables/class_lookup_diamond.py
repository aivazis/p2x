#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable with two parents that share an ancestor finds the trait python would
find, even when the redeclaration comes from the parent listed second
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
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # a saw that runs along a rail
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # the length of the rail
        rail = p2x.traits.properties.float()

    # a saw with a blade of its own
    class FineSaw(PanelSaw):
        """
        A panel saw with a thinner blade
        """

        # the width of its cut, with no other names
        kerf = p2x.traits.properties.float()

    # a saw that is both
    class RailSaw(TrackSaw, FineSaw):
        """
        A fine saw that runs along a rail
        """

    # python puts the second parent ahead of the shared ancestor
    assert RailSaw.__mro__.index(FineSaw) < RailSaw.__mro__.index(PanelSaw)

    # so the name leads to the redeclared trait
    assert RailSaw._p2x_trait("kerf") is FineSaw.__dict__["kerf"]
    # the alias went with the trait it replaced
    assert missing(RailSaw, "cut-width")
    # and the trait of the first parent is still found
    assert RailSaw._p2x_trait("rail") is TrackSaw.__dict__["rail"]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
