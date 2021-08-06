#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

import logging
logger = logging.getLogger("mcni.utils.mpi")

#
import os

ENVVAR_MPI_LAUNCHER = "MCVINE_MPI_LAUNCHER"
mpi_launcher_choice = os.environ.get(ENVVAR_MPI_LAUNCHER, 'mpirun')

ENVVAR_BINDING_NAME = 'MCVINE_MPI_BINDING'
if mpi_launcher_choice == 'serial':
    # if running in serial mode, no point to find a mpi binding
    os.environ[ENVVAR_BINDING_NAME] = 'NONE'
mpi_binding_choice = os.environ.get(ENVVAR_BINDING_NAME)

i# methods
def _find_mpi_binding():
    choices = ['mpi4py', 'pyre']
    for c in choices:
        mod = use_mpi_binding(c)
        if mod: return mod
        continue
    return

def use_mpi_binding(name):
    import importlib
    mod = importlib.import_module('.use_%s' % name, __name__)
    if mod.world:
        return mod


# import binding module
if mpi_binding_choice == 'NONE':
    b = None
elif mpi_binding_choice:
    b = use_mpi_binding(mpi_binding_choice)
else:
    b = _find_mpi_binding()


# expose interface of binding module if it is available
if b:
    names = [
        'size', 'rank', 'world', 
        'send', 'receive',
        'sendStr', 'receiveStr'
        ]
    for name in names:
        exp = '%s = b.%s' % (name, name)
        exec(exp)
        continue
    binding_name = b.name
else:
    name = None
    world = None
    size = rank = 0
    send = receive = None
    sendStr = receiveStr = None
    binding_name = None


# version
__id__ = "$Id$"

# End of file 
