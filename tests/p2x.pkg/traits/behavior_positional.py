#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a behavior given its description in place of its metadata refuses the declaration,
and records what it received, the method it decorates, and where
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
    Make the common mistake of passing a behavior its description positionally
    """
    # the factory of behaviors, of any type, so the type checker lets the mistaken call through
    behavior: typing.Any = p2x.traits.behavior
    # attempt to
    try:
        # declare a saw for cutting panels
        class PanelSaw(p2x.components.component):
            """
            A saw for cutting sheet goods
            """

            # cutting, with its description where the metadata should go
            @behavior("make a cut")
            def cut(self) -> None:
                """
                Make a cut
                """

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by a behavior
        assert isinstance(error, p2x.exceptions.BehaviorError)
        # which knows its name
        assert error.behavior == "PanelSaw.cut"
        # what it received
        assert error.value == "make a cut"
        # and the method it was placed in front of
        assert error.method is not None and error.method.__name__ == "cut"
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
        assert 'behavior("make a cut")' in linecache.getline(__file__, locator.line)
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the mistaken declaration was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
