#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that an alias of a trait that cannot belong to a set is reported like any other alias that
is not a string
"""

# externals
import typing

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Give a trait aliases with a list among them
    """
    # the mistaken alias
    mistake = ["width"]
    # among the aliases, which the type checker would otherwise refuse
    aliases: typing.Any = ("cut-width", mistake)
    # attempt to
    try:
        # declare a saw for cutting panels
        class PanelSaw(p2x.components.configurable):
            """
            A saw for cutting sheet goods
            """

            # the width of the cut
            kerf = p2x.traits.properties.float()
            # with a good alias and one that is a list
            kerf.aliases = aliases

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by an alias
        assert isinstance(error, p2x.exceptions.TraitAliasError)
        # of this trait
        assert error.trait.name == "kerf"
        # that knows what was given
        assert error.value is mistake
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the mistaken alias was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
