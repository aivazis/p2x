#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that the command locator names the command line argument
"""


def test() -> None:
    """
    Render a command locator
    """
    # get the package
    import p2x.tracking

    # make a locator
    locator = p2x.tracking.command(argument="--help")
    # check that it says where the value came from
    assert str(locator) == "from the command line argument '--help'"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
