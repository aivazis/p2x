#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Visitors: each trait is handled by the most specific handler its visitor supplies
"""

# support
import p2x.traits
import p2x.traits.properties


# the shop's spec sheet has a line for every kind of trait
class SpecSheet:
    """
    A visitor that describes each trait in the words of its most specific kind
    """

    def _p2x_onTrait(self, trait: p2x.traits.trait, **kwds) -> str:
        """
        Describe a trait of no particular kind
        """
        # say as much as is known
        return "a setting"

    def _p2x_onProperty(self, trait: p2x.traits.property, **kwds) -> str:
        """
        Describe a property
        """
        # say as much as is known
        return "a simple value"

    def _p2x_onFloat(self, trait: p2x.traits.properties.float, *, unit: str, **kwds) -> str:
        """
        Describe a real number, in the {unit} of the shop
        """
        # a measurement, in the shop's unit
        return f"a measurement in {unit}"


# the test
def test() -> None:
    """
    Visit one trait of each kind with the spec sheet
    """
    # make a spec sheet
    sheet = SpecSheet()

    # a trait of no particular kind gets the generic line
    assert p2x.traits.trait()._p2x_identify(authority=sheet) == "a setting"
    # a property gets the property line
    assert p2x.traits.property()._p2x_identify(authority=sheet) == "a simple value"
    # and a real number gets its own line, with the extra arguments passed through to the handler
    assert (
        p2x.traits.properties.float()._p2x_identify(authority=sheet, unit="mm")
        == "a measurement in mm"
    )

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
