#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
A behavior captures the method it decorates, whether or not the decorator is given arguments
"""

# support
import p2x.traits


# the test
def test() -> None:
    """
    Hand a behavior its method in each of the ways it accepts, and check that it captured it
    """

    # the methods to capture
    def cut(self) -> None:
        """
        Make a cut
        """

    def swap(self) -> None:
        """
        Replace the blade
        """

    def align(self) -> None:
        """
        Line the rail up with a mark
        """

    # decorate one without arguments
    plain = p2x.traits.behavior(cut)
    # another with an argument list, the way metadata is passed
    called = p2x.traits.behavior()(swap)
    # and name the third explicitly
    named = p2x.traits.behavior(default=align)

    # all are behaviors
    assert isinstance(plain, p2x.traits.behavior)
    assert isinstance(called, p2x.traits.behavior)
    assert isinstance(named, p2x.traits.behavior)
    # whose defaults are the methods they were given
    assert plain.default is cut
    assert called.default is swap
    assert named.default is align

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
