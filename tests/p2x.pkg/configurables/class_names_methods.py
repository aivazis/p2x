#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that the methods a configurable declares, of every kind, are found and called as python
would, through the class and through its descendants
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare methods of every kind and call them through the class that declares them and through
    a derived one
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()

        # a plain method
        def cut(self, length: float) -> str:
            """
            Make a cut of the given {length}
            """
            # say what was cut
            return f"cut {length}"

        # a class method
        @classmethod
        def model(cls) -> str:
            """
            Name the model
            """
            # the name of the class says it
            return cls.__name__

        # a static method
        @staticmethod
        def units() -> str:
            """
            Name the units of length
            """
            # always the same
            return "mm"

        # a class attribute holding a nested class
        class Blade:
            """
            The blade of a saw
            """

    # the same saw, mounted on a rail
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # a class method that chains up
        @classmethod
        def model(cls) -> str:
            """
            Name the model, after the one it derives from
            """
            # decorate what my ancestor says
            return f"track {super().model()}"

    # a plain method is the function itself, through the class and its descendants
    assert PanelSaw.cut is PanelSaw.__dict__["cut"]
    assert TrackSaw.cut is PanelSaw.__dict__["cut"]
    # and it can be called with an explicit instance
    assert PanelSaw.cut(None, length=3.2) == "cut 3.2"
    # class methods bind to the class they are reached through, and chain up
    assert PanelSaw.model() == "PanelSaw"
    assert TrackSaw.model() == "track TrackSaw"
    # static methods are plain functions
    assert TrackSaw.units() == "mm"
    # nested classes are plain attributes
    assert TrackSaw.Blade is PanelSaw.__dict__["Blade"]
    # and the trait is still read as a value
    assert TrackSaw.kerf == 0.0

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
