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
    # configurable
    from ..components.Configurable import Configurable


# a name that none of the traits of a configurable answers to
class TraitNotFoundError(P2XError, LookupError):
    """
    Raised when a configurable and its ancestors have no trait that answers to a given alias
    """

    # the message template
    description = "'{error.configurable.__name__}' has no setting named '{error.alias}'"

    # metamethods
    def __init__(self, *, configurable: type[Configurable], alias: str, **kwds) -> None:
        """
        Record the {configurable} that was searched and the {alias} it did not recognize
        """
        # chain up
        super().__init__(**kwds)
        # the class whose traits were searched
        self.configurable = configurable
        # and the name that none of them answers to
        self.alias = alias
        # all done
        return


# end of file
