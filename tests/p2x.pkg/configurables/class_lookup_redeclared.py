#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a trait redeclared in a derived configurable replaces the inherited one, aliases and
all, without disturbing the ancestor
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
    Redeclare a trait that has an alias in a derived configurable, without the alias
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # a saw with a blade of its own
    class FineSaw(PanelSaw):
        """
        A panel saw with a thinner blade
        """

        # the width of its cut, with no other names
        kerf = p2x.traits.properties.float()

    # the derived saw finds its own trait under its name
    assert FineSaw._p2x_trait("kerf") is FineSaw.__dict__["kerf"]
    # but the alias went with the inherited trait
    assert missing(FineSaw, "cut-width")

    # the ancestor still finds its own trait, under both names
    assert PanelSaw._p2x_trait("kerf") is PanelSaw.__dict__["kerf"]
    assert PanelSaw._p2x_trait("cut-width") is PanelSaw.__dict__["kerf"]

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
