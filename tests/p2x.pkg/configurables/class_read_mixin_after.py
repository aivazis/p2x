#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that, when a plain class comes after a configurable in the derivation, its attribute leaves
the inherited trait in place, so the configurable reads the default of the trait
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Derive a configurable from a configurable and a plain class, in that order
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # with a preferred value
        kerf.default = 0.25
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # a plain class with a fixed kerf
    class Fixed:
        """
        A blade that always cuts the same width
        """

        # the width of its cut
        kerf = 0.125

    # a saw with the fixed blade listed last
    class TrackSaw(PanelSaw, Fixed):
        """
        A panel saw with a fixed blade
        """

    # python looks through the configurable before the plain class
    assert TrackSaw.__mro__.index(PanelSaw) < TrackSaw.__mro__.index(Fixed)
    # so the saw reads the default of the trait, under the name
    assert TrackSaw.kerf == 0.25
    # and under the alias
    assert getattr(TrackSaw, "cut-width") == 0.25

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
