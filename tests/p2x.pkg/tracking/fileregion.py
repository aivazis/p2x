#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that the region locator renders the file and both ends of the region
"""


# the test
def test() -> None:
    """
    Render a region whose ends are fully known
    """
    # get the package
    import p2x.tracking

    # the start of the region
    start = p2x.tracking.file(source="script.py", line=16, column=2)
    # and its end
    end = p2x.tracking.file(source="script.py", line=17, column=52)
    # make the region
    region = p2x.tracking.region(start=start, end=end)
    # check that it names the file once and shows both ends
    assert str(region) == "script.py:16:2-17:52"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
