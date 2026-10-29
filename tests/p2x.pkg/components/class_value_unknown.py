#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a class write of a name that no trait answers to makes a plain class attribute
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
    Write a name that is not a trait through the class
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.component):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # with a preferred value
        kerf.default = 0.125

    # write a name no trait answers to
    PanelSaw.blade = "rip"

    # it is a plain class attribute
    assert PanelSaw.__dict__["blade"] == "rip"
    # not a trait
    assert missing(PanelSaw, "blade")
    # and the trait is undisturbed
    assert PanelSaw.kerf == 0.125

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
