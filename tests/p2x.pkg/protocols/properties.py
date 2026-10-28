#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Watch the properties of protocols as Role visits them, in the order they are declared
"""

# support
import p2x.components
import p2x.traits.properties


def test() -> None:
    """
    Declare two protocols with nothing but properties, one derived from the other
    """

    # the shop's specification of a saw
    class Saw(p2x.components.protocol):
        """
        What every saw in the shop must provide
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # how deep it can cut
        depth = p2x.traits.properties.float()

    # a saw that runs along a rail adds a requirement of its own
    class TrackSaw(Saw):
        """
        A saw that runs along a rail
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
