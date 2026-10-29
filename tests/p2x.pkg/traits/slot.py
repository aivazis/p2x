#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a slot holds a value and the locator of where it was set
"""

# support
import p2x.tracking
import p2x.traits


# the test
def test() -> None:
    """
    Fill a slot, then replace its contents
    """
    # make a locator
    here = p2x.tracking.here()
    # and a slot that holds a value set here
    slot = p2x.traits.slot(value=0.125, locator=here)

    # the slot remembers both
    assert slot.value == 0.125
    assert slot.locator is here

    # make another locator
    there = p2x.tracking.here()
    # replace the contents of the slot
    slot.value = 0.25
    slot.locator = there

    # the slot remembers the new ones
    assert slot.value == 0.25
    assert slot.locator is there

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
