# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# superclass
from .Locator import Locator


# a locator for a place in python code
class Script(Locator):
    """
    A locator that records a place in python code: the file, the line, and the function
    """

    # meta methods
    def __init__(
        self, *, source: str, line: int | None = None, function: str | None = None, **kwds
    ) -> None:
        """
        Record the {line} of {source} and the {function} it belongs to
        """
        # chain up
        super().__init__(**kwds)
        # save the file
        self.source = source
        # the line, which may be unknown
        self.line = line
        # and the function, which may be unknown as well
        self.function = function
        # all done
        return

    def __str__(self) -> str:
        """
        Render the place as {source}:{line} in {function}, leaving out what is unknown
        """
        # start with the file
        text = self.source
        # if the line is known
        if self.line is not None:
            # attach it
            text += f":{self.line}"
        # if the function is known
        if self.function is not None:
            # name it
            text += f" in {self.function}"
        # all done
        return text

    # my attributes
    __slots__ = "source", "line", "function"


# end of file
