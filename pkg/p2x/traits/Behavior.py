# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# externals
import typing

# the superclass
from .Trait import Trait


# the base class of traits that capture methods
class Behavior(Trait):
    """
    A trait that captures a method that is part of the external interface of its owner
    """

    # metamethods
    def __new__(cls, default: typing.Callable | None = None, **kwds) -> typing.Any:
        """
        Make a behavior when given its method, a stand in when given anything else, or else a
        decorator that waits for the method
        """
        # when used as a plain decorator, the method is known
        if callable(default):
            # so make a behavior right away
            return super().__new__(cls)

        # anything else in its place is a mistake
        if default is not None:
            # that gets a stand in, which python initializes with my arguments; it derives from
            # me, so it is imported here
            from .Malformed import Malformed

            # make one
            return super().__new__(Malformed)

        # otherwise, i was given my metadata ahead of the method, so hand python a decorator that
        # waits for the method and then makes the behavior with all it knows
        def decorator(method: typing.Callable) -> "Behavior":
            """
            Make a behavior that decorates {method}
            """
            # with the metadata i was given
            return cls(default=method, **kwds)

        # and hand it over
        return decorator

    def __init__(self, default: typing.Callable | None = None, **kwds) -> None:
        """
        Build a behavior descriptor
        """
        # chain up
        super().__init__(default=default, **kwds)
        # all done
        return

    # the descriptor protocol
    def __get__(self, instance: object, owner: type) -> typing.Callable:
        """
        Hand over my method as python does for functions: bound to {instance}, if there is one
        """
        # let my superclass ask the class for my method
        method = super().__get__(instance, owner)
        # when accessed through the class
        if instance is None:
            # hand it over as is
            return method
        # otherwise, bind it to {instance}
        return method.__get__(instance, owner)

    # visiting
    def _p2x_identify(self, authority: typing.Any, **kwds) -> object:
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
