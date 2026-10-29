# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the error raised when a trait is declared more than once
from ..exceptions import TraitRedeclarationError

# the traits i recognize
from ..traits.Trait import Trait


# the storage in which the body of a configurable accumulates its declarations
class SymbolTable(dict):
    """
    The mapping in which the body of a configurable accumulates its declarations, noticing names
    that are bound to a trait more than once
    """

    # metamethods
    def __init__(self, **kwds) -> None:
        """
        Build an empty symbol table
        """
        # chain up
        super().__init__(**kwds)
        # the mistakes noticed while the body runs
        self.errors: list[Exception] = []
        # all done
        return

    def __setitem__(self, name: str, value: object) -> None:
        """
        Bind {name} to {value}, unless {name} already holds a trait
        """
        # if {name} already holds a trait
        if name in self and self._p2x_isTrait(self[name]):
            # binding it again is a mistake
            self.errors.append(
                TraitRedeclarationError(name=name, original=self[name], replacement=value)
            )
        # either way, python's rules apply
        super().__setitem__(name, value)
        # all done
        return

    # implementation details
    def _p2x_isTrait(self, value: object) -> bool:
        """
        Check whether {value} is a trait
        """
        # like python's special methods, the hook is looked up on the type
        try:
            # find out how {value} identifies itself
            identify = type(value)._p2x_identify
        # if it doesn't know how
        except AttributeError:
            # it isn't a trait
            return False
        # otherwise, let it introduce itself
        return identify(value, authority=self)

    # visiting
    def _p2x_onTrait(self, trait: Trait, **kwds) -> bool:
        """
        Acknowledge a {trait}
        """
        # it is one
        return True


# end of file
