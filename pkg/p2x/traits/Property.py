# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# externals
import typing

# the superclass
from .Trait import Trait


# the base class of traits whose values are simple objects
class Property(Trait):
    """
    A trait whose values are simple objects
    """

    # the descriptor protocol
    def __get__(self, instance: object, owner: type) -> object:
        """
        Look up my value in {instance}, or in {owner} when {instance} has none of its own
        """
        # an instance keeps its own value under my name
        if instance is not None and self.name in instance.__dict__:
            # so hand it over
            return instance.__dict__[self.name]
        # otherwise, let my superclass ask the class for my value
        return super().__get__(instance, owner)

    def __set__(self, instance: object, value: object) -> None:
        """
        Make {value} my value in {instance}
        """
        # store it under my name
        instance.__dict__[self.name] = value
        # all done
        return

    def __delete__(self, instance: object) -> None:
        """
        Discard my value in {instance}
        """
        # forget it, whether it was ever set or not
        instance.__dict__.pop(self.name, None)
        # all done
        return

    # visiting
    def _p2x_identify(self, authority: typing.Any, **kwds) -> object:
        """
        Let {authority} know i am a property
        """
        # attempt to
        try:
            # ask {authority} for my handler
            handler = authority._p2x_onProperty
        # if it doesn't understand
        except AttributeError:
            # chain up
            return super()._p2x_identify(authority=authority, **kwds)
        # otherwise, invoke the handler
        return handler(trait=self, **kwds)


# end of file
