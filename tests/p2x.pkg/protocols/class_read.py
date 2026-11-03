#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a protocol class reads the default of its trait, by name and by alias, and so does a
protocol derived from it
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a protocol and read its trait
    """

    # the shop's specification of a saw
    class Saw(p2x.components.protocol):
        """
        What every saw in the shop must provide
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # with a preferred value
        kerf.default = 0.125
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # a narrower specification
    class PanelSaw(Saw):
        """
        What every saw for sheet goods must provide
        """

    # both specifications read the default, under the name and the alias
    for specification in (Saw, PanelSaw):
        assert specification.kerf == 0.125
        assert getattr(specification, "cut-width") == 0.125

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
