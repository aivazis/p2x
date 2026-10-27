# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


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

        # go through the attributes in the order they were declared
        for key, value in attributes.items():
            # interesting attributes know how to identify themselves to a visitor; like python's
            # special methods, the hook is looked up on the type, so classes in the body are boring
            identify = getattr(type(value), "_p2x_identify", None)
            # if this one doesn't
            if identify is None:
                # it is boring
                continue
            # otherwise, let it introduce itself to the record, which is the visitor
            identify(value, authority=record, name=key)

        # all done
        return record

    # visiting
    def _p2x_onTrait(self, trait: object, name: str, **kwds) -> None:
        """
        Visit a {trait} declared under {name}
        """
        # show what was found, for now
        print(f"{self.__name__}: {name} ({type(trait).__name__})")
        # all done
        return


# end of file
