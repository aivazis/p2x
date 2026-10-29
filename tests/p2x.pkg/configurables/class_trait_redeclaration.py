#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that declaring a trait again under the same name in the body of a configurable refuses the
declaration, and records the name and both traits
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare the same trait twice in one body
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
            # with a default
            kerf.default = 0.125

            # and again, further down
            kerf = p2x.traits.properties.float()
            # with another default
            kerf.default = 0.25

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by declaring a trait again
        assert isinstance(error, p2x.exceptions.TraitRedeclarationError)
        # which knows the name
        assert error.name == "kerf"
        # the trait declared first
        assert error.original.default == 0.125
        # and the one that took its place
        assert error.replacement.default == 0.25
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the second declaration was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
