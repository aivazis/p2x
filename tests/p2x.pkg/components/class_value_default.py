#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a class read of a trait that was never set gives the trait's default
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a component with a trait and read its value through the class
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.component):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # with a preferred value
        kerf.default = 0.125

    # nobody has set a value, so the class reads the default
    assert PanelSaw.kerf == 0.125

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
