#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable does not mistake its plain attributes and methods for traits
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# a lookup that should fail
def missing(configurable: type, alias: str) -> bool:
    """
    Check that {configurable} has no trait that answers to {alias}
    """
    # attempt to
    try:
        # look up the trait
        configurable._p2x_trait(alias)
    # if nobody recognizes {alias}
    except p2x.exceptions.TraitNotFoundError as error:
        # make sure the error says who and what
        return error.configurable is configurable and error.alias == alias
    # if the lookup succeeded, it's not missing
    return False


# the test
def test() -> None:
    """
    Declare a configurable with a trait, a constant and a method, and look all three up
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # a constant is plain
        teeth = 60

        # and so is a method
        def clean(self) -> None:
            """
            Clear the sawdust
            """

    # the trait is found
    assert PanelSaw._p2x_trait("kerf") is PanelSaw.__dict__["kerf"]
    # but the constant is not
    assert missing(PanelSaw, "teeth")
    # and neither is the method
    assert missing(PanelSaw, "clean")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
