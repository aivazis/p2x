#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable refuses to hand over a trait under a name none of its traits answers to
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Look up a trait under a name the configurable does not know
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()

    # attempt to
    try:
        # look up a trait under a mistyped name
        PanelSaw._p2x_trait("kerfs")
    # the lookup is refused
    except p2x.exceptions.TraitNotFoundError as error:
        # by the configurable that was searched
        assert error.configurable is PanelSaw
        # because of the name it did not recognize
        assert error.alias == "kerfs"
        # all done
        return

    # finding a trait is a failure
    assert False, "a mistyped name was recognized"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
