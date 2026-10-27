# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# my metaclass
from .Role import Role

# my superclass
from .Configurable import Configurable


# the base of all classes that describe application requirements
class Protocol(Configurable, metaclass=Role):
    """
    Protocols specify what components must provide
    """


# end of file
