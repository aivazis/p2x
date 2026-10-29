#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that reading a name a configurable does not have raises the error python raises, so the
idioms that probe for attributes keep working
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Read names that are neither traits nor attributes of a configurable
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
        # read a name nobody declared
        PanelSaw.blade
    # it's not there, and python says so
    except AttributeError as error:
        # with the details python provides
        assert error.obj is PanelSaw
        assert error.name == "blade"
    # anything else
    else:
        # is a bug
        assert False, "unreachable"

    # the idioms that rely on it work as usual
    assert not hasattr(PanelSaw, "blade")
    assert getattr(PanelSaw, "blade", None) is None
    # including for names python itself probes for
    assert not hasattr(PanelSaw, "__wrapped__")
    assert not hasattr(PanelSaw, "__fspath__")
    # while the trait is there
    assert hasattr(PanelSaw, "kerf")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
