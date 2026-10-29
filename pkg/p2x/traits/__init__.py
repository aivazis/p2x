# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Typed attributes for components and protocols
"""

# the base classes
from .Trait import Trait as trait
from .Property import Property as property

# the methods that are part of the external interface of their owners
from .Behavior import Behavior as behavior

# the holders of trait values
from .Slot import Slot as slot

# end of file
