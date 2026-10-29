#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a derived component reads the value of an inherited trait from its ancestor, and
sees the changes the ancestor makes after the derivation
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Derive a component from another, then change the value of the inherited trait in the
    ancestor
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

    # the same saw, mounted on a rail
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

    # get the trait
    kerf = PanelSaw._p2x_trait("kerf")

    # the derived saw reads the default, like its ancestor
    assert TrackSaw.kerf == 0.125

    # set the value in the ancestor
    PanelSaw.kerf = 0.25

    # the derived saw sees it
    assert TrackSaw.kerf == 0.25
    # and both still find the trait, so the write set a value rather than replacing it
    assert PanelSaw._p2x_trait("kerf") is kerf
    assert TrackSaw._p2x_trait("kerf") is kerf

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
