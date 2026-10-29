#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a derived configurable finds the traits it inherits, by name and by alias
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Derive a configurable from another and look up traits declared by both
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

    # the same saw, mounted on a rail
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # the length of the rail
        rail = p2x.traits.properties.float()
        # also known by another name
        rail.aliases = "rail-length"

    # the derived saw finds its own trait, by name and by alias
    assert TrackSaw._p2x_trait("rail") is TrackSaw.__dict__["rail"]
    assert TrackSaw._p2x_trait("rail-length") is TrackSaw.__dict__["rail"]
    # and the one it inherits, the same way
    assert TrackSaw._p2x_trait("kerf") is PanelSaw.__dict__["kerf"]
    assert TrackSaw._p2x_trait("cut-width") is PanelSaw.__dict__["kerf"]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
