#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Each kind of trait states its preferred default, and users can override it
"""

# support
import p2x.traits
import p2x.traits.properties


# the test
def test() -> None:
    """
    Check the preferred defaults, and the two ways users override them
    """
    # a trait of no particular kind has no preference
    assert p2x.traits.trait().default is None
    # a real number prefers zero
    assert p2x.traits.properties.float().default == 0.0

    # users can override the preference at construction
    assert p2x.traits.properties.float(default=3.2).default == 3.2

    # or by assigning to the default after construction
    kerf = p2x.traits.properties.float()
    kerf.default = 1.5
    # which sticks
    assert kerf.default == 1.5

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
