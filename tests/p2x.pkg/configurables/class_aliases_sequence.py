#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that aliases given as any collection of strings become a set, along with the trait name
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Give traits their aliases in a list, a tuple, a frozen set, and a generator
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut, with aliases in a list
        kerf = p2x.traits.properties.float()
        kerf.aliases = ["cut-width"]

        # how deep it can cut, with aliases in a tuple
        depth = p2x.traits.properties.float()
        depth.aliases = ("cut-depth",)

        # the size of the blade, with aliases in a frozen set
        blade = p2x.traits.properties.float()
        blade.aliases = frozenset({"blade-size"})

        # the speed of the blade, with aliases made on the fly
        speed = p2x.traits.properties.float()
        speed.aliases = (f"blade-{unit}" for unit in ("rpm",))

    # each one ends up a set with the name in it
    assert PanelSaw.__dict__["kerf"].aliases == {"kerf", "cut-width"}
    assert PanelSaw.__dict__["depth"].aliases == {"depth", "cut-depth"}
    assert PanelSaw.__dict__["blade"].aliases == {"blade", "blade-size"}
    assert PanelSaw.__dict__["speed"].aliases == {"speed", "blade-rpm"}

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
