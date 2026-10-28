#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that the script locator renders the file, the line and the function
"""


# the test
def test() -> None:
    """
    Render a script locator that knows its line and function
    """
    # get the package
    import p2x.tracking

    # make a locator
    locator = p2x.tracking.script(source=__file__, function="test", line=16)
    # check that it shows the whole place
    assert str(locator) == f"{__file__}:16 in test"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
