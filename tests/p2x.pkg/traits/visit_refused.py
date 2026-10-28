#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Visitors: an object with no handler for a trait or any of its ancestors is not a visitor
"""

# support
import p2x.exceptions
import p2x.traits
import p2x.traits.properties


# the shop broom sweeps the floor; it knows nothing about traits
class Broom:
    """
    An object that is not a visitor of traits
    """


def test() -> None:
    """
    Ask the broom to visit a real number
    """
    # make a real number
    thickness = p2x.traits.properties.float()
    # make a broom
    broom = Broom()

    # attempt to
    try:
        # have the broom visit the real number
        thickness._p2x_identify(authority=broom)
        # which must fail
        assert False, "unreachable"
    # it is refused
    except p2x.exceptions.NotAVisitorError as error:
        # with a p2x error
        assert isinstance(error, p2x.exceptions.P2XError)
        # that is also a built-in
        assert isinstance(error, NotImplementedError)
        # it remembers who was involved
        assert error.visitor is broom and error.host is thickness
        # it lists the handlers that were sought, most specific first
        assert error.handlers == ("_p2x_onFloat", "_p2x_onProperty", "_p2x_onTrait")
        # get the full report
        report = list(error.report())
        # it starts with the summary
        assert report[0] == str(error)

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
