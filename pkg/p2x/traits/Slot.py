# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the record of where a value was set
from ..tracking import Locator


# the holder of a trait value
class Slot:
    """
    The holder of a trait value and the locator of where it was set
    """

    # metamethods
    def __init__(self, *, value: object, locator: Locator, **kwds) -> None:
        """
        Hold {value}, set at {locator}
        """
        # chain up
        super().__init__(**kwds)
        # my value
        self.value = value
        # and where it was set
        self.locator = locator
        # all done
        return

    # my attributes
    __slots__ = ("value", "locator")


# end of file
