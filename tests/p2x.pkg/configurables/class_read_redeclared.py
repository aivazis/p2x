#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable that redeclares an inherited trait reads the new default, that the
aliases of the replaced trait reach nothing there, and that its ancestor is undisturbed
"""

# support
import p2x.components
import p2x.traits.properties


# a read that should fail
def missing(configurable: type, alias: str) -> bool:
    """
    Check that reading {alias} through {configurable} finds nothing
    """
    # attempt to
    try:
        # read it
        getattr(configurable, alias)
    # if nothing answers to {alias}
    except AttributeError as error:
        # make sure the error says who and what, and that asking agrees
        return (
            error.obj is configurable and error.name == alias and not hasattr(configurable, alias)
        )
    # if the read succeeded, it's not missing
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
        # with a preferred value
        kerf.default = 0.125
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # a saw with a blade of its own
    class FineSaw(PanelSaw):
        """
        A panel saw with a thinner blade
        """

        # the width of its cut, with no other names
        kerf = p2x.traits.properties.float()
        # and a preferred value of its own
        kerf.default = 0.0625

    # under the name, the derived saw reads the default of its own trait
    assert FineSaw.kerf == 0.0625
    # but the alias went with the inherited trait, so it reads nothing there
    assert missing(FineSaw, "cut-width")
    # the ancestor still reads its own default, under both names
    assert PanelSaw.kerf == 0.125
    assert getattr(PanelSaw, "cut-width") == 0.125

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
