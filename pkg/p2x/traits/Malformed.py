# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# externals
import typing

# the superclass
from .Behavior import Behavior

# the error i carry
from ..exceptions import BehaviorError

# and the location it records
from .. import tracking


# a behavior that was given something other than a method
class Malformed(Behavior):
    """
    A behavior that stands in for a mistaken declaration and carries the error that describes it
    """

    # metamethods
    def __init__(self, default: object, **kwds) -> None:
        """
        Record that {default} was given in place of a method
        """
        # chain up, without a method
        super().__init__(default=None, **kwds)
        # describe the mistake, at the declaration that made it: python calls me directly from
        # the body of the class, so it is the frame just above mine
        self.error = BehaviorError(value=default, locator=tracking.here(level=1))
        # all done
        return

    def __call__(self, method: typing.Callable) -> "Malformed":
        """
        Note the {method} that the mistaken declaration was meant to decorate
        """
        # add it to the description of the mistake
        self.error.method = method
        # and keep standing in for it
        return self

    # the descriptor protocol
    def __set_name__(self, owner: type, name: str) -> None:
        """
        Learn the {name} under which i am declared in the body of {owner}
        """
        # chain up
        super().__set_name__(owner, name)
        # and let the error know which declaration is mistaken, by the names the user wrote
        self.error.behavior = f"{owner.__name__}.{name}"
        # all done
        return

    def __get__(self, instance: object, owner: type) -> typing.Callable:
        """
        Refuse to stand in for a method, since i don't have one
        """
        # complain
        raise self.error

    # visiting
    def _p2x_identify(self, authority: typing.Any, **kwds) -> object:
        """
        Let {authority} know i am a malformed behavior
        """
        # attempt to
        try:
            # ask {authority} for my handler
            handler = authority._p2x_onMalformed
        # if it doesn't understand
        except AttributeError:
            # chain up
            return super()._p2x_identify(authority=authority, **kwds)
        # otherwise, invoke the handler
        return handler(trait=self, **kwds)


# end of file
