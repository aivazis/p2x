# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# externals
import typing

# the superclass
from .Property import Property


# properties whose values are real numbers
class Float(Property):
    """
    A property whose values are real numbers
    """

    # metamethods
    def __init__(self, default: float = 0.0, **kwds) -> None:
        """
        Mark a trait as a floating point number
        """
        # chain up, with zero as my preferred default
        super().__init__(default=default, **kwds)
        # all done
        return

    # visiting
    def _p2x_identify(self, authority: typing.Any, **kwds) -> object:
        """
        Let {authority} know i am a float
        """
        # attempt to
        try:
            # ask {authority} for my handler
            handler = authority._p2x_onFloat
        # if it doesn't understand
        except AttributeError:
            # chain up
            return super()._p2x_identify(authority=authority, **kwds)
        # otherwise, invoke the handler
        return handler(trait=self, **kwds)


# end of file
