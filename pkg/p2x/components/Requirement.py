# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# externals
import collections.abc
import typing

# the errors in the declarations of traits
from ..exceptions import (
    TraitAliasAttributeCollisionError,
    TraitAliasCollisionError,
    TraitAliasError,
    TraitEmptyAliasError,
    TraitReuseError,
)

# the storage for the declarations in a class body
from .SymbolTable import SymbolTable


# the base type of classes that capture application requirements and their implementations
class Requirement(type):
    """
    The type of all classes that help capture application requirements and their implementations
    """

    # metamethods
    @classmethod
    def __prepare__(cls, name: str, bases: tuple[type, ...], **kwds) -> SymbolTable:
        """
        Build the storage in which the body of the class {name} accumulates its declarations
        """
        # make one
        return SymbolTable()

    def __new__(
        cls, name: str, bases: tuple[type, ...], attributes: collections.abc.Mapping, **kwds
    ) -> type:
        """
        Build the class record, then visit the traits it declares
        """
        # when called directly, rather than by a class statement, there is no class body to inspect
        # and my attributes are most likely held by some mapping type
        if not isinstance(attributes, SymbolTable):
            # so make an empty symbol table
            table = SymbolTable()
            # copy the declarations into it
            table.update(attributes)
            # and use it from now on
            attributes = table

        # build the record
        record = super().__new__(cls, name, bases, attributes, **kwds)
        # give it a map from the aliases of the traits it declares to their canonical names, to
        # fill as they are visited; the traits themselves live in its {__dict__}, and inherited
        # traits stay with the ancestors that declare them
        record._p2x_namemap = {}

        # mistakes in the declaration are collected, starting with the ones the symbol table
        # noticed while the body ran, and then as the traits are visited, so they can all be
        # reported together
        errors = list(attributes.errors)
        # the names of the plain attributes, which no alias may take
        plain = set()
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
                plain.add(key)
                # and there is nothing more to do
                continue
            # otherwise, let it introduce itself to the record, which is the visitor; this happens
            # outside the {try}, so a mistake in a handler is never mistaken for a boring attribute
            identify(value, authority=record, name=key, errors=errors)

        # with all the aliases known, look for the ones that name a plain attribute of the body
        for alias, canonical in record._p2x_namemap.items():
            # neither one is nearer than the other, so
            if alias in plain:
                # taking the name is a mistake
                errors.append(
                    TraitAliasAttributeCollisionError(
                        alias=alias, trait=attributes[canonical], value=attributes[alias]
                    )
                )

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

    def _p2x_onTrait(self, trait: typing.Any, name: str, errors: list, **kwds) -> object:
        """
        Visit a {trait} declared under {name}
        """
        # a trait belongs to exactly one declaration; if it is someone else's, or mine under
        # another name
        if trait.owner is not self or trait.name != name:
            # binding it here is a mistake
            errors.append(TraitReuseError(trait=trait, configurable=self, name=name))
            # and there is nothing more to learn from it
            return trait

        # the declaration may have left its aliases in any shape
        aliases = trait.aliases
        # a single string is a single alias
        if isinstance(aliases, str):
            # not a pile of letters
            aliases = (aliases,)
        # a mapping would contribute only its keys
        if isinstance(aliases, collections.abc.Mapping):
            # so refuse it whole
            errors.append(TraitAliasError(trait=trait, value=aliases))
            # and go on with none
            aliases = ()
        # anything else must be a collection of strings
        if not isinstance(aliases, collections.abc.Iterable):
            # so refuse it whole
            errors.append(TraitAliasError(trait=trait, value=aliases))
            # and go on with none
            aliases = ()

        # the trait always answers to its name
        repaired = {name}
        # go through the rest
        for alias in aliases:
            # an alias that isn't a string
            if not isinstance(alias, str):
                # is a mistake
                errors.append(TraitAliasError(trait=trait, value=alias))
                # that is left out
                continue
            # an empty one
            if not alias:
                # is a mistake too
                errors.append(TraitEmptyAliasError(trait=trait))
                # that is left out
                continue
            # the rest are kept
            repaired.add(alias)
        # hand the repaired set back to the trait
        trait.aliases = repaired

        # get my namemap
        namemap = self._p2x_namemap
        # go through the aliases of the trait
        for alias in repaired:
            # if another trait in my body already answers to this one
            if alias in namemap:
                # sharing it is a mistake
                errors.append(
                    TraitAliasCollisionError(
                        alias=alias, owner=self.__dict__[namemap[alias]], rival=trait
                    )
                )
                # and the alias stays with its owner
                continue
            # otherwise, file it against the canonical name
            namemap[alias] = name
        # all done
        return trait


# end of file
