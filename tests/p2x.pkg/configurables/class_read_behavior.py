#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable reads the method a behavior decorates, under the name and the alias of
the behavior
"""

# support
import p2x.components
import p2x.traits


# the test
def test() -> None:
    """
    Declare a configurable with a behavior and read it through the class
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # cutting is part of what the saw offers
        @p2x.traits.behavior
        def cut(self) -> None:
            """
            Make a cut
            """

        # also known as sawing
        cut.aliases |= {"saw"}

    # get the method the behavior decorates
    method = PanelSaw.__dict__["cut"].default

    # the saw reads that method, under the name and the alias
    assert PanelSaw.cut is method
    assert getattr(PanelSaw, "saw") is method
    # and {hasattr} finds both names
    assert hasattr(PanelSaw, "cut")
    assert hasattr(PanelSaw, "saw")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
