# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# externals
import typing

# the error raised when a visitor has no handler for me
from ..exceptions import NotAVisitorError


# the base class of the typed attributes of components and protocols
class Trait:
    """
    A typed attribute of components and protocols
    """

    # metamethods
    def __init__(self, default: object = None, **kwds) -> None:
        """
        Make a trait whose value is {default} until something else is assigned to it
        """
        # chain up
        super().__init__(**kwds)
        # my name
        self.name: str | None = None
        # my default value
        self.default = default
        # all done
        return

    # the descriptor protocol
    def __set_name__(self, owner: type, name: str) -> None:
        """
        Learn the {name} under which i am declared in the body of {owner}
        """
        # remember it
        self.name = name
        # all done
        return

    def __get__(self, instance: object, owner: type) -> object:
        """
        Look up my value in {instance}, or hand myself over when accessed through the class
        """
        # when accessed through the class, which keeps me under my name
        if instance is None:
            # hand myself over
            return self
        # an instance keeps my value under my name; one without a value reads my default
        return instance.__dict__.get(self.name, self.default)

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
        Let {authority} know i am a trait
        """
        # attempt to
        try:
            # ask {authority} for my handler
            handler = authority._p2x_onTrait
        # if it doesn't understand
        except AttributeError:
            # it is not a visitor, since we only get here when all alternatives are exhausted
            raise NotAVisitorError(
                visitor=authority,
                host=self,
                # the handlers i and my ancestors asked for, by the naming convention
                handlers=tuple(
                    # the handler named after each class
                    f"_p2x_on{base.__name__}"
                    # along my derivation
                    for base in type(self).__mro__
                    # that takes part in visiting
                    if "_p2x_identify" in base.__dict__
                ),
            ) from None
        # otherwise, invoke the handler
        return handler(trait=self, **kwds)


# end of file
