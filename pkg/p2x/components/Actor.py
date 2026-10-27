# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# my superclass
from .Requirement import Requirement


# the metaclass of components
class Actor(Requirement):
    """
    The type of all classes that provide implementations of application requirements
    """


# end of file
