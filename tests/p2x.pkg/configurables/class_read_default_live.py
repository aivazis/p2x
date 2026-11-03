#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable reads the current default of a trait, including one changed after the
class is built
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Change the default of a trait after its configurable is declared
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
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # the same saw, mounted on a rail
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

    # change the default of the trait, after both saws are built
    PanelSaw._p2x_trait("kerf").default = 0.25

    # both saws read the new one, under the name and the alias
    for saw in (PanelSaw, TrackSaw):
        assert saw.kerf == 0.25
        assert getattr(saw, "cut-width") == 0.25

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
