# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# externals
import collections.abc

# the error raised when a name is not a trait
from ..exceptions import TraitNotFoundError

# the record of where a value was set
from .. import tracking

# the holder of a trait value
from ..traits.Slot import Slot

# my superclass
from .Requirement import Requirement


# the metaclass of components
class Actor(Requirement):
    """
    The type of all classes that provide implementations of application requirements
    """

    # metamethods
    def __new__(
        cls, name: str, bases: tuple[type, ...], attributes: collections.abc.Mapping, **kwds
    ) -> type:
        """
        Build the class record, with room for the values of its traits
        """
        # build the record
        record = super().__new__(cls, name, bases, attributes, **kwds)
        # it holds no values of its own until someone sets them
        record._p2x_slots = {}
        # all done
        return record

    def __setattr__(self, name: str, value: object) -> None:
        """
        Set the value of the trait that answers to {name}, or the plain attribute {name}
        """
        # the framework's names are handled by python, even before my namemap exists
        if name.startswith("_p2x_"):
            # so let it
            return super().__setattr__(name, value)
        # otherwise, attempt to
        try:
            # find the trait that answers to {name}
            trait = self._p2x_trait(name)
        # if there isn't one
        except TraitNotFoundError:
            # it's a plain attribute, which python handles
            return super().__setattr__(name, value)
        # where the value was set
        locator = tracking.here(level=1)
        # get my slots
        slots = self._p2x_slots
        # if i already have a value of my own for {trait}
        if trait.name in slots:
            # get its slot
            slot = slots[trait.name]
            # and replace its contents
            slot.value = value
            slot.locator = locator
            # all done
            return
        # otherwise, give me a slot of my own
        slots[trait.name] = Slot(value=value, locator=locator)
        # all done
        return

    def __delattr__(self, name: str) -> None:
        """
        Discard my value of the trait that answers to {name}, or the plain attribute {name}
        """
        # the framework's names are handled by python
        if name.startswith("_p2x_"):
            # so let it
            return super().__delattr__(name)
        # otherwise, attempt to
        try:
            # find the trait that answers to {name}
            trait = self._p2x_trait(name)
        # if there isn't one
        except TraitNotFoundError:
            # it's a plain attribute, which python handles
            return super().__delattr__(name)
        # discard my value, whether i had one or not, so i inherit again
        self._p2x_slots.pop(trait.name, None)
        # all done
        return


# end of file
