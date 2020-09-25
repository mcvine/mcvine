# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

from __future__ import print_function
from .. import mcvine

@mcvine.group()
def mpi():
    return

@mpi.command()
def launcher():
    from mcni.pyre_support.MpiApplication import mpi_launcher_choice as l
    print(l)
    return

from . import info

# End of file 
