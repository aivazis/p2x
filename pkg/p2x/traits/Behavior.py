# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the superclass
from .Trait import Trait


# the base class of traits that capture methods
class Behavior(Trait):
    """
    A trait that captures a method that is part of the external interface of its owner
    """

    # visiting
    def _p2x_identify(self, authority: object, **kwds) -> object:
        """
        Let {authority} know i am a behavior
        """
        # attempt to
        try:
            # ask {authority} for my handler
            handler = authority._p2x_onBehavior
        # if it doesn't understand
        except AttributeError:
            # chain up
            return super()._p2x_identify(authority=authority, **kwds)
        # otherwise, invoke the handler
        return handler(trait=self, **kwds)


# end of file
