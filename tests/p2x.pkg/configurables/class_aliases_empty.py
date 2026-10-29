#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that an empty string among the aliases of a trait refuses the declaration
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Give a trait an empty alias next to a good one
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
            # with a good alias and an empty one
            kerf.aliases = "cut-width", ""

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by an empty alias
        assert isinstance(error, p2x.exceptions.TraitEmptyAliasError)
        # of this trait
        assert error.trait.name == "kerf"
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the empty alias was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
