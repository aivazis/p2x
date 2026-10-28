#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Watch the behaviors of protocols as Role visits them, in the order they are declared
"""

# support
import p2x.components
import p2x.traits


# the test
def test() -> None:
    """
    Declare two protocols with nothing but behaviors, one derived from the other
    """

    # the shop's specification of a saw
    class Saw(p2x.components.protocol):
        """
        What every saw in the shop must provide
        """

        # every saw must cut
        @p2x.traits.behavior
        def cut(self) -> None:
            """
            Make a cut
            """

        # and let its blade be changed
        @p2x.traits.behavior
        def swap(self) -> None:
            """
            Replace the blade
            """

    # a saw that runs along a rail adds a requirement of its own
    class TrackSaw(Saw):
        """
        A saw that runs along a rail
        """

        # it must line up with a mark before cutting
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
