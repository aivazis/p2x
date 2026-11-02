# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# externals
import collections.abc
import typing

# the error raised when a visitor has no handler for me
from ..exceptions import NotAVisitorError

# the error raised when my value cannot be read
from ..exceptions import TraitReadError

# the record of where my default was set
from .. import tracking

# the holder of my default
from .Slot import Slot


# the base class of the typed attributes of components and protocols
class Trait:
    """
    A typed attribute of components and protocols
    """

    # metamethods
    def __init__(self, default: object = None, **kwds) -> None:
        """
        Build a trait descriptor
        """
        # chain up
        super().__init__(**kwds)
        # the class that declares me
        self.owner: type | None = None
        # my name
        self.name: str | None = None
        # my alternative names; a mistaken declaration leaves them as given, for the class
        # that declares me to refuse
        self._p2x_aliases: typing.Any = set()

        # build a slot for my default value
        self._p2x_slot = Slot(value=default, locator=tracking.unknown())

        # all done
        return

    # my default value
    @property
    def default(self) -> object:
        """
        Get my default value
        """
        # it lives in my slot
        return self._p2x_slot.value

    @default.setter
    def default(self, value: object) -> None:
        """
        Set my default to {value}
        """
        # replace the contents of my slot
        self._p2x_slot.value = value
        # and remember the line that asked for it
        self._p2x_slot.locator = tracking.here(level=1)
        # all done
        return

    # my alternative names
    @property
    def aliases(self) -> set[str]:
        """
        Get my alternative names
        """
        # they live in a set, unless a mistaken declaration left them as given
        return self._p2x_aliases

    @aliases.setter
    def aliases(self, value: str | collections.abc.Iterable[str]) -> None:
        """
        Set my alternative names to {value}, a single name or a collection of them
        """
        # a single string is a single alias, not a pile of letters
        if isinstance(value, str):
            # so it makes a set of one
            self._p2x_aliases = {value}
            # and there is nothing more to do
            return
        # a mapping and anything that isn't a collection are mistakes
        if isinstance(value, collections.abc.Mapping) or not isinstance(
            value, collections.abc.Iterable
        ):
            # held as given, for the class that declares me to refuse
            self._p2x_aliases = value
            # and there is nothing more to do
            return
        # gather the names once, since {value} may be consumed by reading it
        names = tuple(value)
        # if they are all strings
        if all(isinstance(name, str) for name in names):
            # they make a set
            self._p2x_aliases = set(names)
            # and there is nothing more to do
            return
        # otherwise, they are held as given, in order, for the class that declares me to sort out
        self._p2x_aliases = names
        # all done
        return

    # the descriptor protocol
    def __get__(self, instance: object, owner: type) -> object:
        """
        Look up my value in {owner}
        """
        # {owner} knows its values
        read = owner._p2x_read
        # attempt to
        try:
            # ask it for mine
            return read(trait=self)
        # if the read stumbles on a missing attribute, python would take me for missing
        except AttributeError as error:
            # so report the mistake as a failed read
            raise TraitReadError(configurable=owner, trait=self) from error

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Learn the {name} under which i am declared in the body of {owner}
        """
        # i belong to the first declaration that binds me, and the metaclass reports any other
        if self.owner is not None:
            # so i keep the identity i already have
            return
        # otherwise, remember who declares me
        self.owner = owner
        # and under what name
        self.name = name
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
