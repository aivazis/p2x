# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
from collections.abc import Iterator

# the superclass
from .P2XError import P2XError


# an object asked to visit something it has no handlers for
class NotAVisitorError(P2XError, NotImplementedError):
    """
    Raised when a host has exhausted every handler it could ask its visitor for
    """

    # the message template
    description = (
        "'{error.visitor.__class__.__name__}' is not a '{error.host.__class__.__name__}' visitor"
    )

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
        """
        Record the {visitor} that came up short, the {host} it visited, and the {handlers} the
        host asked for
        """
        # chain up
        super().__init__(**kwds)
        # the object that was asked to visit
        self.visitor = visitor
        # the object that was visited
        self.host = host
        # and the names of the handlers the host asked for, in the order it asked
        self.handlers = handlers
        # all done
        return


# end of file
