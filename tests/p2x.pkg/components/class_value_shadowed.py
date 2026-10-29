#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a class write of a name that hides an inherited trait rebinds the plain attribute,
without disturbing the ancestor
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
    Shadow a trait with a plain attribute in a derived component, and write to it
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.component):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # with a preferred value
        kerf.default = 0.125

    # a saw whose kerf is fixed
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # a plain attribute by the name of the trait
        kerf = 0.25

    # and one derived from it
    class RailSaw(TrackSaw):
        """
        A track saw with a longer rail
        """

    # write to the plain attribute
    TrackSaw.kerf = 0.0625

    # it is rebound
    assert TrackSaw.__dict__["kerf"] == 0.0625
    # and seen from below
    assert RailSaw.kerf == 0.0625
    # the trait stays hidden
    assert missing(TrackSaw, "kerf")
    # and the ancestor keeps its trait and its value
    assert PanelSaw._p2x_trait("kerf") is PanelSaw.__dict__["kerf"]
    assert PanelSaw.kerf == 0.125

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
