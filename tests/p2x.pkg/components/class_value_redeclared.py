#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a trait redeclared in a derived component starts from its own default, not from
the value its ancestor set
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Set the value of a trait in a component, then redeclare the trait in a derived one
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
    # the saw still finds the trait, so the write set a value rather than replacing it
    assert PanelSaw._p2x_trait("kerf") is kerf

    # a saw with a blade of its own
    class FineSaw(PanelSaw):
        """
        A panel saw with a thinner blade
        """

        # the width of its cut
        kerf = p2x.traits.properties.float()
        # with a preferred value of its own
        kerf.default = 0.0625

    # the derived saw finds its own trait
    assert FineSaw._p2x_trait("kerf") is FineSaw.__dict__["kerf"]
    # and reads its default
    assert FineSaw.kerf == 0.0625
    # while the ancestor keeps its trait
    assert PanelSaw._p2x_trait("kerf") is kerf
    # and its value
    assert PanelSaw.kerf == 0.25

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
