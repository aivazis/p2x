#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that component classes find their traits, by name and by alias
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a component and look up its trait
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.component):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # the trait is found under its name
    assert PanelSaw._p2x_trait("kerf") is PanelSaw.__dict__["kerf"]
    # and its alias
    assert PanelSaw._p2x_trait("cut-width") is PanelSaw.__dict__["kerf"]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
