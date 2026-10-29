#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a class write of a trait sets its value, and leaves the trait in place
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Set the value of a trait through the class and read it back
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

    # get the trait
    kerf = PanelSaw._p2x_trait("kerf")

    # set the value
    PanelSaw.kerf = 0.25

    # the class reads it back
    assert PanelSaw.kerf == 0.25
    # and the trait is still there
    assert PanelSaw._p2x_trait("kerf") is kerf
    # with its default untouched
    assert kerf.default == 0.125

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
