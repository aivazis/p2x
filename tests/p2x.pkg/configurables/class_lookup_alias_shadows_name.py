#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a derived trait whose alias is the name of an inherited trait wins that name in the
derived configurable, without disturbing the ancestor
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a trait in a derived configurable with an alias that names an inherited trait
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()

    # a saw that measures its cut differently
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # the width of the blade
        width = p2x.traits.properties.float()
        # which is what this saw means by its kerf
        width.aliases |= {"kerf"}

    # the derived saw sends the name to its own trait
    assert TrackSaw._p2x_trait("kerf") is TrackSaw.__dict__["width"]
    # while the ancestor keeps its own
    assert PanelSaw._p2x_trait("kerf") is PanelSaw.__dict__["kerf"]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
