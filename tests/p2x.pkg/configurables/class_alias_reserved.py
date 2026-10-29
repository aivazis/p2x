#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that an alias the framework reserves refuses the declaration
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Give a trait an alias that starts with the framework's prefix, next to a good one
    """
    # attempt to
    try:
        # declare a saw for cutting panels
        class PanelSaw(p2x.components.configurable):
            """
            A saw for cutting sheet goods
            """

            # the width of the cut
            kerf = p2x.traits.properties.float()
            # with a good alias and one that belongs to the framework
            kerf.aliases = "cut-width", "_p2x_width"

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by a reserved name
        assert isinstance(error, p2x.exceptions.TraitReservedNameError)
        # that this trait answers to
        assert error.trait.name == "kerf"
        assert error.name == "_p2x_width"
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the reserved alias was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
