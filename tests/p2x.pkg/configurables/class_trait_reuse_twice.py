#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that binding one trait under two names in the same body refuses the declaration
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Bind a trait under a second name in the body that declares it
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
            # and the same trait under another name
            width = kerf

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by reusing a trait
        assert isinstance(error, p2x.exceptions.TraitReuseError)
        # which belongs to its first name
        assert error.trait.name == "kerf"
        # and was bound again under another
        assert error.name == "width"
        # in the same body
        assert error.configurable is error.trait.owner
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the second name was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
