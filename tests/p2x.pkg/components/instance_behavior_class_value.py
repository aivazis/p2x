#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that an instance calls the method its class was given for a behavior, bound to the
instance, including one the class inherits
"""

# support
import p2x.components
import p2x.traits


# the test
def test() -> None:
    """
    Give a class a new method for a behavior, then call it through instances
    """

    # a saw
    class Saw(p2x.components.component):
        """
        A saw
        """

        # cutting reports what happened
        @p2x.traits.behavior
        def cut(self, length: float) -> str:
            """
            Make a cut of the given {length}
            """
            # say what was cut
            return f"cut {length}"

    # a saw that cuts at an angle
    class MiterSaw(Saw):
        """
        A saw whose cuts are at an angle
        """

    # the instances call the method the behavior decorates
    assert MiterSaw().cut(length=3.2) == "cut 3.2"

    # another way to cut
    def miter(self: Saw, length: float) -> str:
        """
        Make an angled cut of the given {length}
        """
        # say what was cut, and by whom
        return f"{type(self).__name__} mitered {length}"

    # give the derived saw the new method
    MiterSaw.cut = miter

    # its instances call it, bound to themselves
    assert MiterSaw().cut(length=3.2) == "MiterSaw mitered 3.2"
    # while the instances of the ancestor keep the original
    assert Saw().cut(length=3.2) == "cut 3.2"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
