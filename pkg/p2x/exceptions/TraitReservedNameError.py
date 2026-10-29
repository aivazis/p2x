# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the superclass
from .P2XError import P2XError


# a trait that answers to a name the framework reserves
class TraitReservedNameError(P2XError, ValueError):
    """
    Raised when a trait answers to a name the framework reserves, as its name or as an alias
    """

    # the message template
    description = "'{error.name}' is reserved"

    # metamethods
    def __init__(self, *, trait: object, name: str, **kwds) -> None:
        """
        Record the {trait} that answers to the reserved {name}
        """
        # chain up
        super().__init__(**kwds)
        # the trait whose names are mistaken
        self.trait = trait
        # and the name it may not take
        self.name = name
        # all done
        return


# end of file
