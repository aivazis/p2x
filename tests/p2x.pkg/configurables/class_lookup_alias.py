#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable finds each of its traits under every one of its aliases, and that the
name of a trait is always among them
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a configurable with a trait that has aliases and one that doesn't, and look them up
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # also known by more names, listed any way that is convenient
        kerf.aliases = "cut-width", "width"

        # how deep it can cut, under its name alone
        depth = p2x.traits.properties.float()

    # get the traits
    kerf = PanelSaw.__dict__["kerf"]
    depth = PanelSaw.__dict__["depth"]

    # the name is among the aliases, whether others were declared or not
    assert kerf.aliases == {"kerf", "cut-width", "width"}
    assert depth.aliases == {"depth"}

    # every alias leads to its trait
    assert PanelSaw._p2x_trait("kerf") is kerf
    assert PanelSaw._p2x_trait("cut-width") is kerf
    assert PanelSaw._p2x_trait("width") is kerf
    assert PanelSaw._p2x_trait("depth") is depth

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
