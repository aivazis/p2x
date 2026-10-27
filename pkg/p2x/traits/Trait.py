# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the error raised when a visitor has no handler for me
from ..exceptions import NotAVisitorError


# the base class of the typed attributes of components and protocols
class Trait:
    """
    A typed attribute of components and protocols
    """

    # the descriptor protocol
    def __set_name__(self, owner: type, name: str) -> None:
        """
        Learn the {name} under which i am declared in the body of {owner}
        """

    def __get__(self, instance: object, owner: type) -> object:
        """
        Look up my value in {instance}, or in {owner} when accessed through the class
        """

    def __set__(self, instance: object, value: object) -> None:
        """
        Make {value} my value in {instance}
        """

    def __delete__(self, instance: object) -> None:
        """
        Discard my value in {instance}
        """

    # visiting
    def _p2x_identify(self, authority: object, **kwds) -> object:
        """
        Let {authority} know i am a trait
        """
        # attempt to
        try:
            # ask {authority} for my handler
            handler = authority._p2x_onTrait
        # if it doesn't understand
        except AttributeError:
            # it is not a visitor, since we only get here when all alternatives are exhausted
            raise NotAVisitorError(
                visitor=authority,
                host=self,
                # the handlers i and my ancestors asked for, by the naming convention
                handlers=tuple(
                    # the handler named after each class
                    f"_p2x_on{base.__name__}"
                    # along my derivation
                    for base in type(self).__mro__
                    # that takes part in visiting
                    if "_p2x_identify" in base.__dict__
                ),
            ) from None
        # otherwise, invoke the handler
        return handler(trait=self, **kwds)


# end of file
