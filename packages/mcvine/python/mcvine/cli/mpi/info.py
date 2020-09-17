# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, click

from . import mpi
@mpi.command()
def info():
    from mcni.utils import mpi
    print()
    print("* mpi binding: %s" % mpi.binding_name)
    print()
    print("To set mpi binding for mcvine, use env var %r" % mpi.ENVVAR_BINDING_NAME)
    print()
    return


# End of file 
