#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a mapping given as the aliases of a trait refuses the declaration, rather than
contributing its keys
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Give a trait a dictionary as its aliases
    """
    # the mistaken aliases
    aliases = {"cut-width": "the width of the cut"}

    # attempt to
    try:
        # declare a saw for cutting panels
        class PanelSaw(p2x.components.configurable):
            """
            A saw for cutting sheet goods
            """

            # the width of the cut
            kerf = p2x.traits.properties.float()
            # with a dictionary where its aliases go
            kerf.aliases = aliases

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by an alias
        assert isinstance(error, p2x.exceptions.TraitAliasError)
        # of this trait
        assert error.trait.name == "kerf"
        # which is the whole dictionary
        assert error.value is aliases
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the dictionary was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
