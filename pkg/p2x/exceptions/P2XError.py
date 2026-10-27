# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
The base class of every error p2x raises
"""


class P2XError(Exception):
    """
    The base class of every error p2x raises
    """

    # the message template; subclasses must override and fill it in from their own attributes
    description = "an unknown p2x error"

    # interface
    def report(self):
        """
        Generate an error report with the full details of the error
        """
        # my generic error message
        yield str(self)
        # and nothing else
        return

    # metamethods
    def __init__(self, **kwds) -> None:
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
