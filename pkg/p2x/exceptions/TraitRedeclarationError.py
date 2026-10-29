# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# externals
import typing

# the superclass
from .P2XError import P2XError

# the types in my annotations, protected to avoid making cycles
if typing.TYPE_CHECKING:
    # traits
    from ..traits.Trait import Trait


# a name bound to a trait that is bound again in the body of the same class
class TraitRedeclarationError(P2XError, TypeError):
    """
    Raised when a name that holds a trait is bound again in the body of the same class
    """

    # the message template
    description = "'{error.name}' is declared more than once"

    # metamethods
    def __init__(self, *, name: str, original: Trait, replacement: object, **kwds) -> None:
        """
        Record the {name} that was bound again, the {original} trait it held, and the
        {replacement} bound to it later
        """
        # chain up
        super().__init__(**kwds)
        # the name bound twice
        self.name = name
        # the trait declared first
        self.original = original
        # and the one that took its place
        self.replacement = replacement
        # all done
        return


# end of file
