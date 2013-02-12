#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import journal
info = journal.info( 'mcni.utils.mpi' )

import os
mpi_binding_choice = os.environ.get('MCVINE_MPI_BINDING')

def _find_mpi_binding():
    choices = ['mpi4py', 'pyre']
    for c in choices:
        mod = use_mpi_binding(c)
        if mod: return mod
        continue
    return


def use_mpi_binding(name):
    exec "from . import use_%s as mod" % name
    if mod.world:
        return mod

if mpi_binding_choice:
    b = use_mpi_binding(mpi_binding_choice)
else:
    b = _find_mpi_binding()
if b:
    names = ['size', 'rank', 'world', 'send', 'receive']
    for name in names:
        exp = '%s = b.%s' % (name, name)
        exec exp
        continue
else:
    world = None
    size = rank = 0
    send = receive = None


# version
__id__ = "$Id$"

# End of file 
