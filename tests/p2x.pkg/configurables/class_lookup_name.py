#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable finds each of its traits under its name
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a configurable with two traits and look each one up by name
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # how deep it can cut
        depth = p2x.traits.properties.float()

    # each name leads to the trait declared under it
    assert PanelSaw._p2x_trait("kerf") is PanelSaw.__dict__["kerf"]
    assert PanelSaw._p2x_trait("depth") is PanelSaw.__dict__["depth"]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
