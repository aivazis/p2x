#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that {here} records the location of its caller, or of a caller further up when asked,
without reading any source files
"""

# externals
import sys


# a function that asks for locators, so the test can check where they point
def caller() -> tuple:
    """
    Ask for a locator that records this function, and one that records my caller
    """
    # get the package
    import p2x.tracking

    # the line number of the first request
    line = sys._getframe().f_lineno + 2
    # a locator for this function
    mine = p2x.tracking.here()
    # and one for my caller
    theirs = p2x.tracking.here(level=1)
    # hand them off, along with the line of the first
    return mine, theirs, line


# the test
def test() -> None:
    """
    Check the locators {here} builds, and that it opens no files to build them
    """
    # get the package now, so its import is not mistaken for reading source files
    import p2x.tracking

    # the files the test opens
    opened = []

    # record the files that get opened
    def hook(event: str, args: tuple) -> None:
        """
        Watch for file opens
        """
        # if a file is being opened
        if event == "open":
            # record it
            opened.append(args[0])
        # all done
        return

    # watch
    sys.addaudithook(hook)
    # the line of the call below
    line = sys._getframe().f_lineno + 2
    # get the locators
    mine, theirs, callerLine = caller()
    # the first one records the function that asked for it
    assert mine.source == __file__
    assert mine.line == callerLine
    assert mine.function == "caller"
    # the second one records its caller
    assert theirs.source == __file__
    assert theirs.line == line
    assert theirs.function == "test"
    # and nothing was read to build them
    assert not opened, opened
    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
