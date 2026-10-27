# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# my metaclass
from .Actor import Actor

# my superclass
from .Configurable import Configurable


# the base of all classes that implement a particular requirement
class Component(Configurable, metaclass=Actor):
    """
    Components provide implementations of application requirements
    """


# end of file
