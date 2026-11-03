#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a derived configurable reads the defaults of the traits it inherits, by name and by
alias, along with those of its own
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Derive a configurable from another and read traits declared by both
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
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

        # the length of the rail
        rail = p2x.traits.properties.float()
        # with a preferred value
        rail.default = 55.0
        # also known by another name
        rail.aliases = "rail-length"

    # the derived saw reads the default of its own trait, by name and by alias
    assert TrackSaw.rail == 55.0
    assert getattr(TrackSaw, "rail-length") == 55.0
    # and of the trait it inherits, the same way
    assert TrackSaw.kerf == 0.125
    assert getattr(TrackSaw, "cut-width") == 0.125
    # {hasattr} finds all four names
    assert hasattr(TrackSaw, "rail")
    assert hasattr(TrackSaw, "rail-length")
    assert hasattr(TrackSaw, "kerf")
    assert hasattr(TrackSaw, "cut-width")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
