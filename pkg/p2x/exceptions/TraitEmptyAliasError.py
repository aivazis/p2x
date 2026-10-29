# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the superclass
from .P2XError import P2XError


# a trait given an empty string as an alias
class TraitEmptyAliasError(P2XError, ValueError):
    """
    Raised when a trait is given an empty string as an alias
    """

    # the message template
    description = "'{error.trait.name}' has an empty alias"

    # metamethods
    def __init__(self, *, trait: object, **kwds) -> None:
        """
        Record the {trait} that was given an empty alias
        """
        # chain up
        super().__init__(**kwds)
        # the trait whose aliases are mistaken
        self.trait = trait
        # all done
        return


# end of file
