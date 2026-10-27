#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Sanity check: verify that the traits are accessible
"""


def test() -> None:
    """
    Reach the traits
    """
    # access the package
    import p2x.traits

    # the base classes are in the traits package
    assert issubclass(p2x.traits.property, p2x.traits.trait)
    # and so are the behaviors
    assert issubclass(p2x.traits.behavior, p2x.traits.trait)

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
