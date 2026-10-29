# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the superclass
from .P2XError import P2XError


# a trait that already belongs to a declaration, bound again elsewhere
class TraitReuseError(P2XError, TypeError):
    """
    Raised when a trait that already belongs to one declaration is bound under another
    """

    # the message template
    description = (
        "'{error.configurable.__name__}.{error.name}' reuses "
        "'{error.trait.owner.__name__}.{error.trait.name}'"
    )

    # metamethods
    def __init__(self, *, trait: object, configurable: type, name: str, **kwds) -> None:
        """
        Record the {trait}, which knows the declaration it belongs to, and the {configurable}
        that bound it again under {name}
        """
        # chain up
        super().__init__(**kwds)
        # the trait, which knows its owner and its name
        self.trait = trait
        # the class that bound it again
        self.configurable = configurable
        # and the name it was bound under
        self.name = name
        # all done
        return


# end of file
