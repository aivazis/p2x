# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
p2x is a testbed for the design and implementation of pyre 2.x
"""

# version info
from . import meta

# this is expected to be here
__version__ = meta.version


# administrative
def copyright() -> None:
    """
    Print the p2x copyright note
    """
    # show the header, which carries the copyright and the author
    return print(meta.header)


def license() -> None:
    """
    Print the p2x license
    """
    # show the full license text
    return print(meta.license)


def version() -> tuple[int, int, int, str]:
    """
    Return the p2x version
    """
    # hand back the version tuple stamped in at build time
    return meta.version


def credits() -> None:
    """
    Print the acknowledgments
    """
    # show the people and organizations that made this possible
    return print(meta.acknowledgments)


# end of file
