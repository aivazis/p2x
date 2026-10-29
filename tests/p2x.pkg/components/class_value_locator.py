#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a class write of a trait records the line that made it, under its name or an alias
"""

# externals
import sys

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Set the value of a trait through the class, under its name and under its alias
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.component):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # the line of the write below
    line = sys._getframe().f_lineno + 2
    # set the value under the name
    PanelSaw.kerf = 0.25

    # get the locator of the value
    locator = PanelSaw._p2x_slots["kerf"].locator
    # it records the write
    assert locator.source == __file__
    assert locator.line == line
    assert locator.function == "test"

    # the line of the write below
    line = sys._getframe().f_lineno + 2
    # set the value under the alias
    setattr(PanelSaw, "cut-width", 0.125)

    # get the locator of the value
    locator = PanelSaw._p2x_slots["kerf"].locator
    # it records the new write
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
