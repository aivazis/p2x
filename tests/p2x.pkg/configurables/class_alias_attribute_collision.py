#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a trait alias that names a plain attribute in the same body refuses the declaration,
and records the alias, the trait, and the value of the attribute
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Declare a plain attribute and a trait with an alias by the same name
    """
    # attempt to
    try:
        # declare a saw for cutting panels
        class PanelSaw(p2x.components.configurable):
            """
            A saw for cutting sheet goods
            """

            # the number of teeth on the blade
            teeth = 60

            # the width of the cut
            kerf = p2x.traits.properties.float()
            # also known by the name of the attribute
            kerf.aliases = "teeth"

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by an alias that names an attribute
        assert isinstance(error, p2x.exceptions.TraitAliasAttributeCollisionError)
        # which knows the alias
        assert error.alias == "teeth"
        # the trait that answers to it
        assert error.trait.name == "kerf"
        # and the value of the attribute
        assert error.value == 60
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the alias was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
