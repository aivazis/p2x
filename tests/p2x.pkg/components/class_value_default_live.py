#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a class read of a trait that was never set follows changes to the trait's default
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Change the default of a trait after its component is declared
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

    # change the default
    PanelSaw._p2x_trait("kerf").default = 0.25

    # nobody has set a value, so both read the new default
    assert PanelSaw.kerf == 0.25
    assert TrackSaw.kerf == 0.25

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
