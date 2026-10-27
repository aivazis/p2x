# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
The error raised when an object is asked to visit something it has no handlers for
"""

# support
from collections.abc import Iterator

# the superclass
from .P2XError import P2XError


class NotAVisitorError(P2XError, NotImplementedError):
    """
    Raised when a host has exhausted every handler it could ask its visitor for
    """

    # the message template
    description = "'{error.visitorType}' is not a '{error.hostType}' visitor"

    # interface
    def report(self) -> Iterator[str]:
        """
        Generate an error report with the full details of the error
        """
        # start with the summary
        yield str(self)
        # identify the host that was visited
        yield f"  while visiting: {self.host!r}"
        # and the visitor that came up short
        yield f"  by: {self.visitor!r}"
        # explain what would have satisfied the host
        yield "  a visitor must implement at least one of these handlers, most specific first:"
        # go through the handlers the host asked for
        for handler in self.handlers:
            # and list each one
            yield f"    {handler}"
        # all done
        return

    # metamethods
    def __init__(self, *, visitor: object, host: object, handlers: tuple[str, ...], **kwds) -> None:
        # chain up
        super().__init__(**kwds)
        # the object that was asked to visit
        self.visitor = visitor
        # the object that was visited
        self.host = host
        # the names of the handlers the host asked for, in the order it asked
        self.handlers = handlers
        # the fully qualified name of the type of the visitor
        self.visitorType = f"{type(visitor).__module__}.{type(visitor).__qualname__}"
        # and of the type of the host
        self.hostType = f"{type(host).__module__}.{type(host).__qualname__}"
        # all done
        return


# end of file
