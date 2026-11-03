# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved

# the names that the build stamps into meta.py from meta.py.in, for the type checker, which reads
# the sources and never sees the expanded module

# when the package was built
date: str
# the parts of the version
major: int
minor: int
micro: int
revision: str
# and the version they make
version: tuple[int, int, int, str]

# decorations for the help system
copyright: str
banner: str
header: str
license: str
acknowledgments: str

# end of file
