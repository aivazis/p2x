# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the superclass
from .P2XError import P2XError


# two traits in the body of one class that answer to the same alias
class TraitAliasCollisionError(P2XError, TypeError):
    """
    Raised when two traits declared in the body of the same class answer to the same alias
    """

    # the message template
    description = (
        "'{error.rival.name}' is aliased to '{error.alias}', "
        "but this name already belongs to '{error.owner.name}'"
    )

    # metamethods
    def __init__(self, *, alias: str, owner: object, rival: object, **kwds) -> None:
        """
        Record the {alias}, the {owner} that answered to it first, and the {rival} declared
        after it that tried to
        """
        # chain up
        super().__init__(**kwds)
        # the name that is claimed twice
        self.alias = alias
        # the trait it already belongs to
        self.owner = owner
        # and the one that tried to take it
        self.rival = rival
        # all done
        return


# end of file
