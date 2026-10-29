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
    # configurables
    from ..components.Configurable import Configurable

    # traits
    from ..traits.Trait import Trait


# a trait whose value could not be read
class TraitReadError(P2XError, RuntimeError):
    """
    Raised when reading the value of a trait fails with an error that python would take for a
    missing attribute
    """

    # the message template
    description = "'{error.configurable.__name__}.{error.trait.name}' could not be read"

    # metamethods
    def __init__(self, *, configurable: type[Configurable], trait: Trait, **kwds) -> None:
        """
        Record the {trait} whose value {configurable} could not read
        """
        # chain up
        super().__init__(**kwds)
        # the class whose value was asked for
        self.configurable = configurable
        # and the trait
        self.trait = trait
        # all done
        return


# end of file
