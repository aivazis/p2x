#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that two traits in the body of a configurable that answer to the same alias refuse the
declaration, and record the alias and the traits that share it
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare two traits that share an alias
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
            # also known as its width
            kerf.aliases |= {"width"}

            # the width of a panel it can take
            capacity = p2x.traits.properties.float()
            # also known as its width
            capacity.aliases |= {"width"}

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by sharing an alias
        assert isinstance(error, p2x.exceptions.TraitAliasCollisionError)
        # which knows the alias
        assert error.alias == "width"
        # the trait it already belonged to
        assert error.owner.name == "kerf"
        # and the one that tried to take it
        assert error.rival.name == "capacity"
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the shared alias was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
