# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the superclass
from .P2XError import P2XError


# a trait given an alias that is not a string
class TraitAliasError(P2XError, TypeError):
    """
    Raised when a trait is given an alias that is not a string
    """

    # the message template
    description = (
        "the aliases of '{error.trait.name}' must be strings, "
        "not '{error.value.__class__.__name__}' like {error.value!r}"
    )

    # metamethods
    def __init__(self, *, trait: object, value: object, **kwds) -> None:
        """
        Record the {trait} and the {value} it was given as an alias
        """
        # chain up
        super().__init__(**kwds)
        # the trait whose aliases are mistaken
        self.trait = trait
        # and the value that is not a string
        self.value = value
        # all done
        return


# end of file
