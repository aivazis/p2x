#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that the file locator renders the file and the position within it
"""


def test() -> None:
    """
    Render a file locator that knows its line and column
    """
    # get the package
    import p2x.tracking

    # make a locator
    locator = p2x.tracking.file(source="script.py", line=16, column=2)
    # check that it shows the whole position
    assert str(locator) == "script.py:16:2"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
