#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Watch the properties of components as Actor visits them, in the order they are declared
"""

# support
import p2x.components
import p2x.traits.properties


def test() -> None:
    """
    Declare two components with nothing but properties, one derived from the other
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.component):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # how deep it can cut
        depth = p2x.traits.properties.float()

    # the same saw, mounted on a rail, adds a setting of its own
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # the length of the rail
        rail = p2x.traits.properties.float()

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
