#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a configurable that hides an inherited trait behind a plain attribute reads the
attribute under the name, from there down, and nothing under the aliases, while its ancestor is
undisturbed
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
    Shadow a trait with a plain attribute in a derived configurable, and derive from that
    """

    # a saw for cutting panels
    class PanelSaw(p2x.components.configurable):
        """
        A saw for cutting sheet goods
        """

        # the width of the cut
        kerf = p2x.traits.properties.float()
        # with a preferred value
        kerf.default = 0.25
        # also known by another name
        kerf.aliases |= {"cut-width"}

    # a saw whose kerf is fixed
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

        # a plain attribute by the name of the trait
        kerf = 0.125

    # and one derived from it
    class RailSaw(TrackSaw):
        """
        A track saw with a longer rail
        """

    # in the saw that hides the trait, and in the one below it
    for saw in (TrackSaw, RailSaw):
        # the name reaches the plain attribute
        assert saw.kerf == 0.125
        # while the alias reaches nothing
        assert missing(saw, "cut-width")
    # the ancestor still reads the default, under both names
    assert PanelSaw.kerf == 0.25
    assert getattr(PanelSaw, "cut-width") == 0.25

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
