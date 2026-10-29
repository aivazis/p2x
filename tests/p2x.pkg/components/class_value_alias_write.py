#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a class write under an alias sets the value of the trait that answers to it
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Set the value of a trait through the class, under its alias, and read it under its name
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
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # the same saw, mounted on a rail
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

    # get the trait
    kerf = PanelSaw._p2x_trait("kerf")

    # set the value under the alias
    setattr(PanelSaw, "cut-width", 0.25)
    # the class reads it under the name
    assert PanelSaw.kerf == 0.25
    # and still finds the trait under both, so the write set a value rather than binding the alias
    assert PanelSaw._p2x_trait("kerf") is kerf
    assert PanelSaw._p2x_trait("cut-width") is kerf

    # the alias works for inherited traits too
    setattr(TrackSaw, "cut-width", 0.0625)
    # so the derived saw has its own value
    assert TrackSaw.kerf == 0.0625
    # and the ancestor keeps its own
    assert PanelSaw.kerf == 0.25
    # both still find the trait under both names
    assert PanelSaw._p2x_trait("kerf") is kerf
    assert PanelSaw._p2x_trait("cut-width") is kerf
    assert TrackSaw._p2x_trait("kerf") is kerf
    assert TrackSaw._p2x_trait("cut-width") is kerf

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
