#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Calling a behavior through its class runs the method it decorates
"""

# support
import p2x.traits


def test() -> None:
    """
    Call a decorated method through the class, the way a subclass reaches its base
    """

    # a saw, kept simple so no metaclass takes part
    class Saw:
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

    # call it through the class, with an explicit instance
    assert Saw.cut(Saw(), length=3.2) == "cut 3.2"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
