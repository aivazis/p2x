# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
The package that contains the basic building blocks
"""

# the metaclasses
from .Requirement import Requirement as requirement
from .Role import Role as role
from .Actor import Actor as actor

# the base classes
from .Configurable import Configurable as configurable
from .Protocol import Protocol as protocol
from .Component import Component as component

# end of file
