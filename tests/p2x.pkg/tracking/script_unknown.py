#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that the script locator leaves out the parts of the location that are unknown
"""


# the test
def test() -> None:
    """
    Render script locators with an unknown line, an unknown function, and both
    """
    # get the package
    import p2x.tracking

    # a locator that knows only the file
    locator = p2x.tracking.script(source="script.py")
    # names only the file
    assert str(locator) == "script.py"

    # one that knows the line but not the function
    locator = p2x.tracking.script(source="script.py", line=16)
    # leaves the function out
    assert str(locator) == "script.py:16"

    # and one that knows the function but not the line
    locator = p2x.tracking.script(source="script.py", function="test")
    # leaves the line out
    assert str(locator) == "script.py in test"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
