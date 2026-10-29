#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable built by calling its metaclass directly finds its traits, just like one
built by a class statement
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Build a configurable without a class statement and look up its trait
    """
    # the width of the cut
    kerf = p2x.traits.properties.float()

    # build a saw for cutting panels by calling the metaclass
    PanelSaw = p2x.components.requirement(
        "PanelSaw", (p2x.components.configurable,), {"kerf": kerf}
    )

    # the trait learned its name
    assert kerf.name == "kerf"
    # and is found under it
    assert PanelSaw._p2x_trait("kerf") is kerf

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
