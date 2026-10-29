#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that binding a trait that belongs to another configurable refuses the declaration, and
leaves the trait with the identity it already had
"""

# support
import p2x.components
import p2x.exceptions
import p2x.traits.properties


# the test
def test() -> None:
    """
    Bind the trait of one configurable in the body of another
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()

    # get the trait
    kerf = PanelSaw.__dict__["kerf"]

    # attempt to
    try:
        # declare a saw that borrows the trait under another name
        class TrackSaw(PanelSaw):
            """
            A panel saw that runs along a rail
            """

            # the width of its cut, borrowed
            width = kerf

    # the declaration is refused
    except ExceptionGroup as group:
        # because of a single mistake
        (error,) = group.exceptions
        # made by reusing a trait
        assert isinstance(error, p2x.exceptions.TraitReuseError)
        # this one
        assert error.trait is kerf
        # in the body of the saw that borrowed it
        assert error.configurable.__name__ == "TrackSaw"
        # under the name it was bound to
        assert error.name == "width"
        # while the trait still belongs to its first declaration
        assert kerf.owner is PanelSaw
        # under its first name
        assert kerf.name == "kerf"
        # all done
        return

    # accepting the declaration is a failure
    assert False, "the borrowed trait was accepted"


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
