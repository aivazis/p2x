# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# superclass
from .Locator import Locator


# a locator for a position within a file
class File(Locator):
    """
    A locator that records a position within a file
    """

    # interface
    def position(self) -> str:
        """
        Render whatever is known of my position as {line}:{column}, with a question mark for a
        line that is unknown while the column is known
        """
        # if the column is unknown
        if self.column is None:
            # the position is the line, which may be unknown as well
            return "?" if self.line is None else str(self.line)
        # otherwise, the line comes first, even if it is unknown
        line = "?" if self.line is None else self.line
        # followed by the column
        return f"{line}:{self.column}"

    # meta methods
    def __init__(
        self, *, source: str, line: int | None = None, column: int | None = None, **kwds
    ) -> None:
        """
        Record the {line} and {column} of a position within {source}
        """
        # chain up
        super().__init__(**kwds)
        # save the file
        self.source = source
        # and the position within it, either part of which may be unknown
        self.line = line
        self.column = column
        # all done
        return

    def __str__(self) -> str:
        """
        Render the file and whatever is known of the position within it
        """
        # if nothing is known about the position
        if self.line is None and self.column is None:
            # the file says it all
            return self.source
        # otherwise, attach the position to the file
        return f"{self.source}:{self.position()}"

    # my attributes
    __slots__ = "source", "line", "column"


# end of file
