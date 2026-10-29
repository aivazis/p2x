#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a trait declared under a name the framework reserves refuses the declaration
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a trait under a name that starts with the framework's prefix
    """
    # attempt to
    try:
        # declare a saw for cutting panels
        class PanelSaw(p2x.components.configurable):
            """
            A saw for cutting sheet goods
            """

            # the width of the cut, under a name that belongs to the framework
            _p2x_kerf = p2x.traits.properties.float()

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by a reserved name
        assert isinstance(error, p2x.exceptions.TraitReservedNameError)
        # that this trait answers to
        assert error.trait.name == "_p2x_kerf"
        assert error.name == "_p2x_kerf"
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the reserved name was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
