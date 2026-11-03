#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable reads the default of a trait under each of its aliases
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a configurable with a trait that has aliases and one that doesn't, and read them
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
        # also known by more names
        kerf.aliases = "cut-width", "width"
        # how deep it can cut, under its name alone
        depth = p2x.traits.properties.float()
        # with a preferred value
        depth.default = 2.5

    # under an alias spelled like a python name, the saw reads the default
    assert PanelSaw.width == 0.125
    # under one that isn't, it reads the same through {getattr}
    assert getattr(PanelSaw, "cut-width") == 0.125
    # {hasattr} finds both aliases
    assert hasattr(PanelSaw, "width")
    assert hasattr(PanelSaw, "cut-width")
    # and the trait without aliases is read under its name
    assert PanelSaw.depth == 2.5

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
