#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that the region locator leaves out the parts of its ends that are unknown
"""


# the test
def test() -> None:
    """
    Render a region whose start has no column and whose end has no line
    """
    # get the package
    import p2x.tracking

    # the start of the region, without a column
    start = p2x.tracking.file(source="script.py", line=16)
    # and its end, without a line
    end = p2x.tracking.file(source="script.py", column=52)
    # make the region
    region = p2x.tracking.region(start=start, end=end)
    # check that each end shows only what is known about it, holding the place of an unknown line
    assert str(region) == "script.py:16-?:52"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
