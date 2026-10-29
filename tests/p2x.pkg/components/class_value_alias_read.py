#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a class read under an alias gives the value of the trait that answers to it
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Read the value of a trait through the class, under its alias, before and after it is set
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
        # also known by another name
        kerf.aliases = {"cut-width"}

    # the same saw, mounted on a rail
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

    # the alias reads the default, in the declaring class and below it
    assert getattr(PanelSaw, "cut-width") == 0.125
    assert getattr(TrackSaw, "cut-width") == 0.125

    # set the value under the name, in the derived saw
    TrackSaw.kerf = 0.25

    # the alias reads it there
    assert getattr(TrackSaw, "cut-width") == 0.25
    # and the ancestor's value is untouched
    assert getattr(PanelSaw, "cut-width") == 0.125

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
