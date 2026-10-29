#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a default given by the constructor, whether the preference of the kind of trait or an
argument, records an unknown location
"""

# support
import p2x.tracking
import p2x.traits
import p2x.traits.properties


# the test
def test() -> None:
    """
    Build traits with the preferred default and with one given as an argument
    """
    # what an unknown location looks like
    unknown = str(p2x.tracking.unknown())

    # a trait with the preference of its kind
    kerf = p2x.traits.properties.float()
    # records an unknown location
    assert str(kerf._p2x_slot.locator) == unknown

    # a trait with a default given to its constructor
    depth = p2x.traits.properties.float(default=2.5)
    # records an unknown location too
    assert str(depth._p2x_slot.locator) == unknown

    # a behavior, whose default is the method it decorates
    @p2x.traits.behavior
    def cut() -> None:
        """
        Make a cut
        """

    # records an unknown location as well
    assert str(cut._p2x_slot.locator) == unknown

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
