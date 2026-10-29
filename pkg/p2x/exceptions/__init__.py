# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
The p2x exception hierarchy
"""

# the root
from .P2XError import P2XError

# visiting
from .NotAVisitorError import NotAVisitorError

# declaring traits
from .BehaviorError import BehaviorError
from .TraitAliasError import TraitAliasError
from .TraitEmptyAliasError import TraitEmptyAliasError
from .TraitAliasCollisionError import TraitAliasCollisionError
from .TraitAliasAttributeCollisionError import TraitAliasAttributeCollisionError
from .TraitReservedNameError import TraitReservedNameError
from .TraitRedeclarationError import TraitRedeclarationError
from .TraitReuseError import TraitReuseError

# looking up traits
from .TraitNotFoundError import TraitNotFoundError

# reading trait values
from .TraitReadError import TraitReadError

# end of file
