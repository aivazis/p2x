#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that the framework's names are reachable through every configurable class, that each
class keeps its own namemap, and that the metaclass's methods do not leak to instances
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Reach the framework's names through a configurable and one derived from it
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()

    # the same saw, mounted on a rail
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

    # every class keeps a namemap of its own, even one that declares nothing
    assert "_p2x_namemap" in vars(PanelSaw)
    assert "_p2x_namemap" in vars(TrackSaw)
    assert vars(PanelSaw)["_p2x_namemap"] is not vars(TrackSaw)["_p2x_namemap"]
    # the lookup is reachable through both
    assert TrackSaw._p2x_trait("kerf") is vars(PanelSaw)["kerf"]

    # the methods of the metaclass are reachable through the class
    assert TrackSaw._p2x_read(trait=vars(PanelSaw)["kerf"]) == 0.0
    # but not through an instance
    assert not hasattr(TrackSaw(), "_p2x_read")
    # nor are they in the attribute dictionaries of the classes
    assert "_p2x_read" not in vars(PanelSaw)
    assert "_p2x_read" not in vars(TrackSaw)

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
