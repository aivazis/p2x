#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Sanity check: verify that the component base class and its metaclass are accessible
"""


# the test
def test() -> None:
    """
    Reach the component base class and its metaclass
    """
    # access the package
    import p2x.components

    # check the metaclass
    assert type(p2x.components.component) is p2x.components.actor

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
