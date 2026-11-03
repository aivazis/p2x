#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable reads its plain attributes and methods as python gives them, beside
the default of its trait
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a configurable with a trait, a constant and a method, and read all three
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # with a preferred value
        kerf.default = 0.125
        # a constant is plain
        teeth = 60

        # and so is a method
        def clean(self) -> str:
            """
            Clear the sawdust
            """
            # say what happened
            return "clean"

    # the saw reads the default of its trait
    assert PanelSaw.kerf == 0.125
    # the value of its constant
    assert PanelSaw.teeth == 60
    # and its method, as the function itself
    assert PanelSaw.clean is PanelSaw.__dict__["clean"]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
