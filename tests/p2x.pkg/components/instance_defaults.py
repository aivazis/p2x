#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
A component instance without a value of its own reads the default, and reading leaves it alone
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Read the defaults of a component whose traits were declared in both styles
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.component):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut, with its default given at construction
        kerf = p2x.traits.properties.float(default=3.2)

        # how deep it can cut, with its default assigned after the declaration
        depth = p2x.traits.properties.float()
        depth.default = 50.0

        # the angle of the blade, left at the default its kind prefers
        bevel = p2x.traits.properties.float()

    # make a saw
    saw = PanelSaw()
    # it reads each default
    assert saw.kerf == 3.2
    assert saw.depth == 50.0
    assert saw.bevel == 0.0
    # without acquiring values of its own
    assert "kerf" not in saw.__dict__
    assert "depth" not in saw.__dict__
    assert "bevel" not in saw.__dict__

    # reading through the class gives the default as well
    assert PanelSaw.kerf == 3.2
    # and the trait still keeps it
    assert PanelSaw._p2x_trait("kerf").default == 3.2

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
