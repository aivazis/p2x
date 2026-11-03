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

# types
import typing

# support
import p2x.components
import p2x.exceptions
import p2x.tracking
import p2x.traits


# the test
def test() -> None:
    """
    Declare a behavior whose implementation is a number
    """
    # the number, of any type, so the type checker lets the mistake through
    mistake: typing.Any = 60
    # attempt to
    try:
        # declare a saw for cutting panels
        class PanelSaw(p2x.components.component):
            """
            A saw for cutting sheet goods
            """

            # the number of teeth, mistaken for something the saw does
            teeth = p2x.traits.behavior(mistake)

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by a behavior
        assert isinstance(error, p2x.exceptions.BehaviorError)
        # which knows its name
        assert error.behavior == "PanelSaw.teeth"
        # and what it received
        assert error.value is mistake
        # but has no method, since it decorates nothing
        assert error.method is None
        # the declaration is located in a script
        locator = error.locator
        assert isinstance(locator, p2x.tracking.script)
        # this file
        assert locator.source == __file__
        # in the body of the class
        assert locator.function == "PanelSaw"
        # on a known line
        assert locator.line is not None
        # the one that holds the mistake
        assert "behavior(mistake)" in linecache.getline(__file__, locator.line)
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the mistaken declaration was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
