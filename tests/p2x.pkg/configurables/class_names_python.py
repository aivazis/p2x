#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that the attributes python gives every class read as python defines them
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a configurable and read the attributes python gives it
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

    # the names
    assert TrackSaw.__name__ == "TrackSaw"
    assert TrackSaw.__qualname__ == "test.<locals>.TrackSaw"
    assert TrackSaw.__module__ == __name__
    # the documentation
    assert TrackSaw.__doc__.strip() == "A panel saw that runs along a rail"
    # the derivation
    assert TrackSaw.__bases__ == (PanelSaw,)
    assert TrackSaw.__mro__[:3] == (TrackSaw, PanelSaw, p2x.components.configurable)
    assert issubclass(TrackSaw, PanelSaw)
    # the type
    assert type(TrackSaw) is type(PanelSaw)
    assert isinstance(TrackSaw, p2x.components.requirement)
    # the attribute dictionaries
    assert "kerf" in vars(PanelSaw)
    assert "kerf" not in vars(TrackSaw)
    # and the listing of names, which includes the inherited trait
    assert "kerf" in dir(TrackSaw)

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
