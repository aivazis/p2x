# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the error raised when an alias is not recognized
from ..exceptions import TraitNotFoundError

# my metaclass
from .Requirement import Requirement


# the base of all classes whose state and methods form the fundamental configuration units
class Configurable(metaclass=Requirement):
    """
    The base of all classes that shape the framework configuration services
    """

    # trait lookup
    @classmethod
    def _p2x_trait(cls, alias: str) -> object:
        """
        Given an {alias}, attempt to look up the associated trait descriptor
        """
        # one walk suffices because {Requirement} keeps the invariants proven sufficient in
        # doc/design/components/trait-lookup.md
        # the ancestors already passed, which are nearer to me than the one being examined
        passed = []
        # go through my ancestors, in {mro} order
        for base in cls.__mro__:
            # asking for their namemap; carefully, because not all bases may have one
            namemap = vars(base).get("_p2x_namemap", {})
            # if {alias} is known
            if alias in namemap:
                # get the canonical name of its trait
                canonical = namemap[alias]
                # if a nearer ancestor holds that name, it hides the trait
                if any(canonical in vars(nearer) for nearer in passed):
                    # so nobody recognizes {alias}
                    break
                # otherwise, look up the trait descriptor and return
                return vars(base)[canonical]
            # if {alias} is a plain attribute here, it hides any trait further up
            if alias in vars(base):
                # so nobody recognizes {alias}
                break
            # remember this one
            passed.append(base)
        # if we get this far, nobody recognized the {alias}
        raise TraitNotFoundError(configurable=cls, alias=alias)


# end of file
