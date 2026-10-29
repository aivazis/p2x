#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable finds its behaviors the same way it finds its properties, since they
all share one namespace
"""

# support
import p2x.components
import p2x.traits
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a configurable with a property and a behavior, and look both up by name and alias
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()

        # cutting is part of what the saw offers
        @p2x.traits.behavior
        def cut(self) -> None:
            """
            Make a cut
            """

        # also known as sawing
        cut.aliases |= {"saw"}

    # the property is found
    assert PanelSaw._p2x_trait("kerf") is PanelSaw.__dict__["kerf"]
    # and so is the behavior, under its name
    assert PanelSaw._p2x_trait("cut") is PanelSaw.__dict__["cut"]
    # and its alias
    assert PanelSaw._p2x_trait("saw") is PanelSaw.__dict__["cut"]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
