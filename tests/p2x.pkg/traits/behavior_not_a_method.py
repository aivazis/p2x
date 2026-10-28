#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a behavior given a value instead of a method refuses the declaration, and records
what it received and where
"""

# to read back the line a locator names
import linecache

# support
import p2x.components
import p2x.exceptions
import p2x.traits


def test() -> None:
    """
    Declare a behavior whose implementation is a number
    """
    # attempt to
    try:
        # declare a saw for cutting panels
        class PanelSaw(p2x.components.component):
            """
            A saw for cutting sheet goods
            """

            # the number of teeth, mistaken for something the saw does
            teeth = p2x.traits.behavior(60)

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by a behavior
        assert isinstance(error, p2x.exceptions.BehaviorError)
        # which knows its name
        assert error.behavior == "PanelSaw.teeth"
        # and what it received
        assert error.value == 60
        # but has no method, since it decorates nothing
        assert error.method is None
        # the declaration is in this file
        assert error.locator.source == __file__
        # in the body of the class
        assert error.locator.function == "PanelSaw"
        # on the line that holds the mistake
        assert "behavior(60)" in linecache.getline(__file__, error.locator.line)
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the mistaken declaration was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
