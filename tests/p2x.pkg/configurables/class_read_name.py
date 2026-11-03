#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable reads the default of a trait under the trait's name
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a configurable with two traits and read each one by name
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
        # how deep it can cut
        depth = p2x.traits.properties.float()
        # with a preferred value
        depth.default = 2.5

    # under each name, the saw reads the default of the trait declared there
    assert PanelSaw.kerf == 0.125
    assert PanelSaw.depth == 2.5
    # it reads the same through {getattr}
    assert getattr(PanelSaw, "kerf") == 0.125
    assert getattr(PanelSaw, "depth") == 2.5
    # and {hasattr} finds both names
    assert hasattr(PanelSaw, "kerf")
    assert hasattr(PanelSaw, "depth")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
