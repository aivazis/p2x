#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that names that are not traits behave as python would when reached through an instance of
a component, and that writes to an instance leave its class alone
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Read, write and delete names of every kind through an instance of a component
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.component):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # a plain class attribute
        blade = "rip"

        # a plain method
        def cut(self, length: float) -> str:
            """
            Make a cut of the given {length}
            """
            # say what was cut
            return f"cut {length}"

    # make a saw
    saw = PanelSaw()

    # its class is the component
    assert type(saw) is PanelSaw
    assert saw.__class__ is PanelSaw
    # methods bind to it
    assert saw.cut(length=3.2) == "cut 3.2"
    # class attributes are visible through it
    assert saw.blade == "rip"

    # writing a plain attribute shadows the class attribute for this instance only
    saw.blade = "crosscut"
    assert saw.blade == "crosscut"
    assert PanelSaw.blade == "rip"
    # and deleting it reveals the class attribute again
    del saw.blade
    assert saw.blade == "rip"

    # reading a name nobody declared is the error python raises
    assert not hasattr(saw, "fence")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
