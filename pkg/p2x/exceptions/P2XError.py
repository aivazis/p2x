# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
from collections.abc import Iterator


# the root of the p2x errors
class P2XError(Exception):
    """
    The base class of every error p2x raises
    """

    # the message template; subclasses must override and fill it in from their own attributes
    description = "an unknown p2x error"

    # interface
    def report(self) -> Iterator[str]:
        """
        Generate an error report with the full details of the error
        """
        # my generic error message
        yield str(self)
        # and nothing else
        return

    # metamethods
    def __init__(self, **kwds) -> None:
        """
        Make an error; subclasses record what describes it
        """
        # chain up
        super().__init__(**kwds)
        # all done
        return

    def __str__(self) -> str:
        """
        Render my message template using my attributes
        """
        # fill in the template
        return self.description.format(error=self)


# end of file
