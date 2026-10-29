#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that protocol classes find their traits, by name and by alias
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a protocol and look up its trait
    """

    # the shop's specification of a saw
    class Saw(p2x.components.protocol):
        """
        What every saw in the shop must provide
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # the trait is found under its name
    assert Saw._p2x_trait("kerf") is Saw.__dict__["kerf"]
    # and its alias
    assert Saw._p2x_trait("cut-width") is Saw.__dict__["kerf"]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
