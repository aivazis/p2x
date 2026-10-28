# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# superclass
from .Locator import Locator


# a locator for a command line argument
class Command(Locator):
    """
    A locator that records a command line argument
    """

    # meta methods
    def __init__(self, *, argument: str, **kwds) -> None:
        """
        Record the command line {argument}
        """
        # chain up
        super().__init__(**kwds)
        # save the argument
        self.argument = argument
        # all done
        return

    def __str__(self) -> str:
        """
        Render the argument
        """
        # say where the value came from
        return f"from the command line argument {self.argument!r}"

    # my attributes
    __slots__ = ("argument",)


# end of file
