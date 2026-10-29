# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the superclass
from .P2XError import P2XError


# a trait alias that names a plain attribute in the body of the same class
class TraitAliasAttributeCollisionError(P2XError, TypeError):
    """
    Raised when a trait answers to an alias that names a plain attribute in the body of the same
    class
    """

    # the message template
    description = (
        "'{error.trait.name}' is aliased to '{error.alias}', "
        "but this name already belongs to an attribute"
    )

    # metamethods
    def __init__(self, *, alias: str, trait: object, value: object, **kwds) -> None:
        """
        Record the {alias}, the {trait} that answers to it, and the {value} of the attribute that
        holds the name
        """
        # chain up
        super().__init__(**kwds)
        # the name both claim
        self.alias = alias
        # the trait that answers to it
        self.trait = trait
        # and the value of the attribute that holds it
        self.value = value
        # all done
        return


# end of file
