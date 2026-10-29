#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Watch the behaviors of components as Actor visits them, in the order they are declared
"""

# support
import p2x.components
import p2x.traits


# the test
def test() -> None:
    """
    Declare two components with nothing but behaviors, one derived from the other
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.component):
        """
        A saw for cutting sheet goods
        """

        # cutting is part of what the saw offers
        @p2x.traits.behavior
        def cut(self) -> None:
            """
            Make a cut
            """

        # and so is changing the blade
        @p2x.traits.behavior
        def swap(self) -> None:
            """
            Replace the blade
            """

    # the same saw, mounted on a rail, adds a behavior of its own
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # it can be lined up with a mark before cutting
        @p2x.traits.behavior
        def align(self) -> None:
            """
            Line the rail up with a mark
            """

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
