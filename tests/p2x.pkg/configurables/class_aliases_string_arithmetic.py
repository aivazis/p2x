#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that aliases given as a single string can be extended with set arithmetic
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Give a trait a single string as its alias, then add another with set arithmetic
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # also known by another name
        kerf.aliases = "cut-width"
        # and one more
        kerf.aliases |= {"width"}

    # the trait answers to its name and both aliases
    assert PanelSaw.__dict__["kerf"].aliases == {"kerf", "cut-width", "width"}

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
