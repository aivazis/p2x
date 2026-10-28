#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a chain renders a location followed by the one that caused it
"""


def test() -> None:
    """
    Chain two simple locators
    """
    # get the package
    import p2x.tracking

    # the most recent location
    first = p2x.tracking.simple(source="first")
    # and the one that caused it
    second = p2x.tracking.simple(source="second")
    # link them
    chain = p2x.tracking.chain(this=first, next=second)
    # check that the chain starts with the most recent location
    assert str(chain) == "first, second"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
