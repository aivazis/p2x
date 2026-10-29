#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that an instance without a value of its own reads the value of its class, including one
the class inherits, and that a value of its own takes precedence
"""

# support
import p2x.components
import p2x.traits.properties


# the test
def test() -> None:
    """
    Set class values, then build instances and read them
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

    # the same saw, mounted on a rail
    class TrackSaw(PanelSaw):
        """
        A panel saw that runs along a rail
        """

    # set the value in the ancestor
    PanelSaw.kerf = 0.25

    # an instance of the ancestor reads the value of its class
    assert PanelSaw().kerf == 0.25
    # and so does an instance of the derived saw, which inherits it
    assert TrackSaw().kerf == 0.25

    # set the value in the derived saw
    TrackSaw.kerf = 0.0625
    # make a saw
    saw = TrackSaw()
    # it reads the value of its own class
    assert saw.kerf == 0.0625

    # give it a value of its own
    saw.kerf = 0.5
    # which takes precedence
    assert saw.kerf == 0.5
    # and leaves the classes alone
    assert TrackSaw.kerf == 0.0625
    assert PanelSaw.kerf == 0.25

    # discard it
    del saw.kerf
    # and the instance reads the value of its class again
    assert saw.kerf == 0.0625

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
