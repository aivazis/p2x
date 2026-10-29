#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a default set by assignment records the line of the assignment, whether in a class
body or not
"""

# externals
import sys

# support
import p2x.traits.properties


# the test
def test() -> None:
    """
    Assign defaults to traits in a class body and in a function, and check where they point
    """

    # a class body that declares a trait
    class Saw:
        """
        A holder of a trait declaration
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # the line of the assignment below
        line = sys._getframe().f_lineno + 2
        # with a preferred value
        kerf.default = 0.125

    # get the locator of the default
    locator = Saw.__dict__["kerf"]._p2x_slot.locator
    # it records the assignment in the class body
    assert locator.source == __file__
    assert locator.line == Saw.line
    assert locator.function == "Saw"

    # make a trait outside any class body
    depth = p2x.traits.properties.float()
    # the line of the assignment below
    line = sys._getframe().f_lineno + 2
    # give it a preferred value
    depth.default = 2.5

    # get the locator of the default
    locator = depth._p2x_slot.locator
    # it records the assignment in this function
    assert locator.source == __file__
    assert locator.line == line
    assert locator.function == "test"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
