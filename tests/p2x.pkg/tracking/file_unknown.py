#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that the file locator leaves out what is unknown, and holds the place of an unknown line
when the column is known
"""


def test() -> None:
    """
    Render file locators with an unknown position, an unknown column, and an unknown line
    """
    # get the package
    import p2x.tracking

    # a locator that knows only the file
    locator = p2x.tracking.file(source="script.py")
    # names only the file
    assert str(locator) == "script.py"

    # one that knows the line but not the column
    locator = p2x.tracking.file(source="script.py", line=16)
    # leaves the column out
    assert str(locator) == "script.py:16"

    # one that knows the column but not the line
    locator = p2x.tracking.file(source="script.py", column=52)
    # holds the place of the line
    assert str(locator) == "script.py:?:52"

    # and one in the first column, which counts from zero
    locator = p2x.tracking.file(source="script.py", line=16, column=0)
    # keeps the column
    assert str(locator) == "script.py:16:0"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
