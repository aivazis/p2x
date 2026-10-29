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
        # build a map (namemap: alias -> name) with the aliases of the locally declared traits
        namemap = record._p2x_initializeNamemap(symbols=attributes)

        # if the class declaration bumped into any mistakes
        if attributes.errors:
            # report them all at once
            raise ExceptionGroup(
                f"mistakes in the declaration of {record.__name__}", attributes.errors
            )

        # attach the namemap
        record._p2x_namemap = namemap

        # all done
        return record

    # initializers of the record state
    def _p2x_initializeNamemap(self, *, symbols: SymbolTable) -> dict[str, str]:
        """
        Build a map of trait aliases to their canonical name, i.e. the name by which they
        are known in the class attribute dictionary
        """
        # create the name map
        namemap = {}
        # create a pile with the name of regular attributes
        plain = set()

        # go through the {symbols} harvested from the class body
        for key, value in symbols.items():
            # our trait descriptors know how to identify themselves, so attempt to
            try:
                # find out whether this particular one does; formulate the question
                # carefully to minimize any crosstalk from its implementation
                identify = type(value)._p2x_identify
            # if {value} doesn't know how to identify itself
            except AttributeError:
                # it is a plain attribute
                plain.add(key)
                # that requires no further processing
                continue
            # otherwise, it's one of ours; ask it to identify itself
            identify(value, authority=self, name=key, namemap=namemap, errors=symbols.errors)

        # with the aliases harvested, look for names that conflict with {plain} attributes
        for alias, canonical in namemap.items():
            # if this {alias} conflicts with a {plain} attribute
            if alias in plain:
                # this is almost certainly a bug in my declaration
                symbols.errors.append(
                    TraitAliasAttributeCollisionError(
                        alias=alias, trait=symbols[canonical], value=symbols[alias]
                    )
                )
        # hand off the populated {namemap}
        return namemap

    # trait values
    def _p2x_read(self, *, trait: typing.Any) -> object:
        """
        Look up the value of {trait} in my class record
        """
        # no class holds a value of its own yet, so every read ends at the default of {trait}
        return trait.default

    # trait recognition
    def _p2x_onMalformed(self, trait: typing.Any, errors: list, **kwds) -> object:
        """
        Set aside the error carried by a malformed {trait}
        """
        # add it to the pile
        errors.append(trait.error)
        # all done
        return trait

    def _p2x_onTrait(
        self, trait: typing.Any, name: str, namemap: dict[str, str], errors: list, **kwds
    ) -> object:
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
                # that is ignored
                continue
            # an empty string
            if not alias:
                # is also a mistake
                errors.append(TraitEmptyAliasError(trait=trait))
                # that is ignored
                continue
            # the rest are kept
            repaired.add(alias)
        # hand the repaired set back to the trait
        trait.aliases = repaired

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
