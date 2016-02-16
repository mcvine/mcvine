# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


__doc__ = """
command line interface
"""

import click

# map aliases to long commands
aliases = dict()

@click.group()
def mcvine():
    return

from . import mpi, sampleassembly #, kernel
from mcvine.instrument import cli
from mcstas2 import cli

# aliases should be the last
from . import bash_aliases

# version
__id__ = "$Id$"

# End of file 
