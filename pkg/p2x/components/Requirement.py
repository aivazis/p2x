# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# externals
import typing


# the base type of classes that capture application requirements and their implementations
class Requirement(type):
    """
    The type of all classes that help capture application requirements and their implementations
    """

    # metamethods
    def __new__(cls, name: str, bases: tuple[type, ...], attributes: dict, **kwds) -> type:
        """
        Build the class record, then visit the traits it declares
        """
        # build the record
        record = super().__new__(cls, name, bases, attributes, **kwds)

        # mistakes in the declaration are collected as the traits are visited, so they can all be
        # reported together
        errors = []
        # go through the attributes in the order they were declared
        for key, value in attributes.items():
            # interesting attributes know how to identify themselves to a visitor; like python's
            # special methods, the hook is looked up on the type, so classes in the body are boring
            try:
                # find out how this one identifies itself
                identify = type(value)._p2x_identify
            # if it doesn't know how
            except AttributeError:
                # it is boring
                continue
            # otherwise, let it introduce itself to the record, which is the visitor; this happens
            # outside the {try}, so a mistake in a handler is never mistaken for a boring attribute
            identify(value, authority=record, name=key, errors=errors)

        # if the declaration had mistakes
        if errors:
            # report them all at once
            raise ExceptionGroup(f"mistakes in the declaration of {record.__name__}", errors)

        # all done
        return record

    # visiting
    def _p2x_onMalformed(self, trait: typing.Any, errors: list, **kwds) -> object:
        """
        Set aside the error carried by a malformed {trait}
        """
        # add it to the pile
        errors.append(trait.error)
        # all done
        return trait

    def _p2x_onTrait(self, trait: object, name: str, **kwds) -> object:
        """
        Visit a {trait} declared under {name}
        """
        # show what was found, for now
        print(f"{self.__name__}: {name} ({type(trait).__name__})")
        # all done
        return trait


# end of file
