# -*- makefile -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# p2x consists of a python package
p2x.packages := p2x.pkg
# and test suites
p2x.tests := p2x.pkg.tests

# load the packages
include $(p2x.packages)
# the test suites
include $(p2x.tests)


# end of file
