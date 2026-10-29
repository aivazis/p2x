#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a plain attribute named after an inherited trait hides the trait, under its name and
all its aliases, from there down, without disturbing the ancestor
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
    Shadow a trait with a plain attribute in a derived configurable, and derive from that
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

    # a saw whose kerf is fixed
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # a plain attribute by the name of the trait
        kerf = 0.125

    # and one derived from it
    class RailSaw(TrackSaw):
        """
        A track saw with a longer rail
        """

    # the trait is gone from the saw that hides it, under its name and its alias
    assert missing(TrackSaw, "kerf")
    assert missing(TrackSaw, "cut-width")
    # and from the ones below it
    assert missing(RailSaw, "kerf")
    assert missing(RailSaw, "cut-width")

    # the ancestor still finds it, under both names
    assert PanelSaw._p2x_trait("kerf") is PanelSaw.__dict__["kerf"]
    assert PanelSaw._p2x_trait("cut-width") is PanelSaw.__dict__["kerf"]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
