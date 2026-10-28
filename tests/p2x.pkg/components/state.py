#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Each instance of a component keeps its own trait values; the class keeps the trait
"""

# support
import p2x.components
import p2x.traits.properties


def test() -> None:
    """
    Set, read and discard the value of a trait on two instances of the same component
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.component):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()

    # the class hands over the trait, which knows the name it was declared under
    assert isinstance(PanelSaw.kerf, p2x.traits.properties.float)
    assert PanelSaw.kerf.name == "kerf"

    # make two saws
    thin = PanelSaw()
    thick = PanelSaw()
    # neither has a kerf yet
    assert thin.kerf is None
    assert thick.kerf is None

    # give each one its own
    thin.kerf = 1.5
    thick.kerf = 3.2
    # and verify they kept them apart
    assert thin.kerf == 1.5
    assert thick.kerf == 3.2

    # discard the kerf of one of them
    del thin.kerf
    # it is uninitialized again
    assert thin.kerf is None
    # while the other one is untouched
    assert thick.kerf == 3.2
    # discarding a value that isn't there is harmless
    del thin.kerf

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
