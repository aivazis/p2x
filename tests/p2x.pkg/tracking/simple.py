#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that the simple locator renders its source
"""


def test() -> None:
    """
    Render a simple locator
    """
    # get the package
    import p2x.tracking

    # make a locator
    locator = p2x.tracking.simple(source="simple")
    # check that it names its source and nothing else
    assert str(locator) == "simple"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
