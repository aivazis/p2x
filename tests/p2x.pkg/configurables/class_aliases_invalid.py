#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that aliases that are neither a string nor a collection of strings refuse the declaration
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Give a trait a number as its aliases
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
            # with a number where its aliases go
            kerf.aliases = 3.5

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by an alias
        assert isinstance(error, p2x.exceptions.TraitAliasError)
        # of this trait
        assert error.trait.name == "kerf"
        # which is not a string
        assert error.value == 3.5
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the mistaken aliases were accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
