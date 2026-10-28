# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
from collections.abc import Iterator

# the superclass
from .P2XError import P2XError

# where the mistake was made
from ..tracking import Locator


# a behavior given a value without saying what it is for
class BehaviorError(P2XError, TypeError):
    """
    Raised when a behavior is given a value without the keyword that specifies what it is for
    """

    # the message template
    description = (
        "{error.behavior} received {error.value!r} "
        "without the keyword that specifies what it is for"
    )

    # interface
    def report(self) -> Iterator[str]:
        """
        Generate an error report with the full details of the error
        """
        # start with the summary
        yield str(self)
        # place the declaration
        yield f"  declared at {self.locator}"
        # and, if it came along later, the method it was meant to decorate
        if self.method is not None:
            # name it
            yield f"  in front of: '{self.method.__qualname__}'"
        # all done
        return

    # metamethods
    def __init__(self, *, value: object, locator: Locator, **kwds) -> None:
        """
        Record the {value} the behavior was given in place of its method, and the {locator} of
        the declaration
        """
        # chain up
        super().__init__(**kwds)
        # the object the behavior was given in place of its method
        self.value = value
        # where the declaration is
        self.locator = locator
        # the behavior is anonymous until it is placed in the body of a class
        self.behavior = "a behavior"
        # and the method it was meant to decorate shows up only if it was used as a decorator
        self.method = None
        # all done
        return


# end of file
