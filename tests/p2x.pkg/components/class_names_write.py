#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that writing and deleting names of a component class that are not traits behaves as python
would: plain attributes, methods, the framework's names, and the attributes python gives every
class
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Write and delete names of every kind through a component class
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.component):
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

    # get the trait
    kerf = PanelSaw._p2x_trait("kerf")

    # a plain attribute lands in the class that was written
    TrackSaw.blade = "rip"
    assert vars(TrackSaw)["blade"] == "rip"
    assert "blade" not in vars(PanelSaw)
    # and goes away when deleted
    del TrackSaw.blade
    assert not hasattr(TrackSaw, "blade")

    # deleting a name the class does not have is the error python raises
    try:
        # delete a name nobody declared
        del TrackSaw.blade
    # python says it's not there
    except AttributeError:
        # as expected
        pass
    # anything else
    else:
        # is a bug
        assert False, "unreachable"

    # a method attached after the fact
    def cut(self, length: float) -> str:
        """
        Make a cut of the given {length}
        """
        # say what was cut
        return f"cut {length}"

    # is a plain attribute
    TrackSaw.cut = cut
    assert vars(TrackSaw)["cut"] is cut
    # that binds to instances, as python does
    assert TrackSaw().cut(length=3.2) == "cut 3.2"

    # names of the framework land in the class that was written
    TrackSaw._p2x_marker = "framework"
    assert vars(TrackSaw)["_p2x_marker"] == "framework"
    # and go away when deleted
    del TrackSaw._p2x_marker
    assert "_p2x_marker" not in vars(TrackSaw)

    # the attributes python gives every class can be written
    TrackSaw.__doc__ = "A saw on a rail"
    assert TrackSaw.__doc__ == "A saw on a rail"
    TrackSaw.__qualname__ = "RailSaw"
    assert TrackSaw.__qualname__ == "RailSaw"

    # and none of this disturbed the trait
    assert PanelSaw._p2x_trait("kerf") is kerf
    assert TrackSaw._p2x_trait("kerf") is kerf
    assert TrackSaw.kerf == 0.0

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
