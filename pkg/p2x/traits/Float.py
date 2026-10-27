# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the superclass
from .Property import Property


# properties whose values are real numbers
class Float(Property):
    """
    A property whose values are real numbers
    """

    # visiting
    def _p2x_identify(self, authority: object, **kwds) -> object:
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
