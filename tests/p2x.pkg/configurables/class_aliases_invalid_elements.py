#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that every alias of a trait that is not a string is reported, each in an error of its own
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
    Give a trait aliases with two mistakes among them
    """
    # a good alias and two that are not strings, of any type, so the type checker lets the
    # mistakes through
    aliases: typing.Any = ("cut-width", 3.5, None)
    # attempt to
    try:
        # declare a saw for cutting panels
        class PanelSaw(p2x.components.configurable):
            """
            A saw for cutting sheet goods
            """

            # the width of the cut
            kerf = p2x.traits.properties.float()
            # with the mistaken aliases
            kerf.aliases = aliases

    # the declaration is refused
    except ExceptionGroup as group:
        # because of two mistakes
        first, second = group.exceptions
        # both made by an alias
        assert isinstance(first, p2x.exceptions.TraitAliasError)
        assert isinstance(second, p2x.exceptions.TraitAliasError)
        # of this trait
        assert first.trait.name == "kerf"
        assert second.trait.name == "kerf"
        # in the order they were given
        assert first.value == 3.5
        assert second.value is None
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the mistaken aliases were accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
