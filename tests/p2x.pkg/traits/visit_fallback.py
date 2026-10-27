#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Visitors: a trait whose own handler is missing falls back to the handlers of its ancestors
"""

# support
import p2x.traits
import p2x.traits.properties


# the labeler marks every simple value the same way, whatever its kind
class Labeler:
    """
    A visitor that only knows about properties
    """

    def _p2x_onProperty(self, trait: p2x.traits.property, **kwds) -> p2x.traits.property:
        """
        Label a property by handing it back
        """
        # the trait that reached me
        return trait


def test() -> None:
    """
    Visit a real number with a visitor that has no handler for real numbers
    """
    # make a real number
    thickness = p2x.traits.properties.float()

    # the labeler has no handler for real numbers, so the property handler takes it
    assert thickness._p2x_identify(authority=Labeler()) is thickness

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
