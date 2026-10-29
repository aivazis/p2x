#!/usr/bin/env python3
# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Verify that a trait whose value cannot be read is not mistaken for a missing attribute
"""

# externals
import types

# support
import p2x.components
import p2x.exceptions
import p2x.traits


# a read that should fail
def unreadable(configurable: type, alias: str) -> bool:
    """
    Check that reading {alias} through {configurable} reports a trait that cannot be read
    """
    # attempt to
    try:
        # read the value
        getattr(configurable, alias)
    # if the read failed as expected
    except p2x.exceptions.TraitReadError as error:
        # make sure the error says who and what, and carries the original mistake
        return (
            error.configurable is configurable
            and error.trait is configurable._p2x_trait(alias)
            and isinstance(error.__cause__, AttributeError)
        )
    # if the read succeeded, or failed some other way, it's not what we expect
    return False


# the test
def test() -> None:
    """
    Declare a trait whose default names a class its module does not have
    """
    # a module that lacks the class a default names
    archives = types.ModuleType("archives")

    # a trait whose default is computed when it is read
    class Late(p2x.traits.property):
        """
        A trait whose default is looked up when it is read
        """

        # my default value
        @property
        def default(self) -> object:
            """
            Look up my default
            """
            # it names something that isn't there
            return archives.S3

    # a component with such a trait
    class Archive(p2x.components.component):
        """
        A store of data products
        """

        # the service that holds the products
        provider = Late()
        # also known by another name
        provider.aliases = "storage"

    # reading it fails, under its name and its alias, without passing for a missing attribute
    assert unreadable(Archive, "provider")
    assert unreadable(Archive, "storage")

    # so asking whether it is there does not hide the mistake either
    try:
        # ask
        hasattr(Archive, "provider")
    # the mistake surfaces
    except p2x.exceptions.TraitReadError:
        # as expected
        pass
    # anything else
    else:
        # is a bug
        assert False, "the unreadable trait passed for a missing attribute"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
