# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# superclass
from .Locator import Locator

# the ends of a region
from .File import File


# a locator for a region of a file
class FileRegion(Locator):
    """
    A locator that records a region of a file, delimited by two file locators
    """

    # meta methods
    def __init__(self, *, start: File, end: File, **kwds) -> None:
        """
        Record the region from {start} to {end}, both positions within the same file
        """
        # chain up
        super().__init__(**kwds)
        # save the two ends of the region
        self.start = start
        self.end = end
        # all done
        return

    def __str__(self) -> str:
        """
        Render the region as {source}:{start}-{end}
        """
        # both ends are in the same file, so name it once
        return f"{self.start.source}:{self.start.position()}-{self.end.position()}"

    # my attributes
    __slots__ = "start", "end"


# end of file
