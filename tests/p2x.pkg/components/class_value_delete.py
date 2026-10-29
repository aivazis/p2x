#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that deleting the value a component set for an inherited trait makes it inherit again
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Set the value of an inherited trait in a derived component and delete it, with and without
    a value set in the ancestor
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

    # set the value in the derived saw
    TrackSaw.kerf = 0.25
    # which still finds the trait, so the write set a value rather than replacing it
    assert TrackSaw._p2x_trait("kerf") is kerf
    # delete it
    del TrackSaw.kerf
    # nobody has a value, so the derived saw reads the default
    assert TrackSaw.kerf == 0.125
    # and both still find the trait, so the deletion took the value rather than the trait
    assert PanelSaw._p2x_trait("kerf") is kerf
    assert TrackSaw._p2x_trait("kerf") is kerf

    # set the value in both
    PanelSaw.kerf = 0.0625
    TrackSaw.kerf = 0.25
    # which still find the trait
    assert PanelSaw._p2x_trait("kerf") is kerf
    assert TrackSaw._p2x_trait("kerf") is kerf
    # delete it from the derived saw
    del TrackSaw.kerf
    # which now reads its ancestor's value
    assert TrackSaw.kerf == 0.0625
    # and both still find the trait
    assert PanelSaw._p2x_trait("kerf") is kerf
    assert TrackSaw._p2x_trait("kerf") is kerf

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
