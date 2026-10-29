#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a plain attribute named after an alias of an inherited trait hides that alias alone
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
    Shadow one alias of a trait with a plain attribute in a derived configurable
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # also known by two other names
        kerf.aliases |= {"cut-width", "width"}

    # a saw with a plain attribute by the name of one of the aliases
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # the width of the rail
        width = 3

    # and one derived from it
    class RailSaw(TrackSaw):
        """
        A track saw with a longer rail
        """

    # get the trait
    kerf = PanelSaw.__dict__["kerf"]

    # the hidden alias is gone from the saw that hides it
    assert missing(TrackSaw, "width")
    # and from the ones below it
    assert missing(RailSaw, "width")

    # the name and the other alias still work in both
    for saw in (TrackSaw, RailSaw):
        assert saw._p2x_trait("kerf") is kerf
        assert saw._p2x_trait("cut-width") is kerf

    # and the ancestor still finds the trait under all three names
    assert PanelSaw._p2x_trait("kerf") is kerf
    assert PanelSaw._p2x_trait("cut-width") is kerf
    assert PanelSaw._p2x_trait("width") is kerf

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
