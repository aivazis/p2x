#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable that hides one alias of an inherited trait behind a plain attribute reads
the attribute under that alias, from there down, and the default under the other names of the trait
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Shadow one alias of a trait with a plain attribute in a derived configurable
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
        # also known by two other names
        kerf.aliases |= {"cut-width", "width"}

    # a saw with a plain attribute named after one of the aliases
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # the width of the rail
        width = 3

    # and one derived from it
    class RailSaw(TrackSaw):
        """
        A track saw with a longer rail
        """

    # in the saw that hides the alias, and in the one below it
    for saw in (TrackSaw, RailSaw):
        # the hidden alias reaches the plain attribute
        assert saw.width == 3
        # while the name and the other alias reach the default
        assert saw.kerf == 0.125
        assert getattr(saw, "cut-width") == 0.125

    # and the ancestor reads the default, under all three names
    assert PanelSaw.kerf == 0.125
    assert PanelSaw.width == 0.125
    assert getattr(PanelSaw, "cut-width") == 0.125

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
