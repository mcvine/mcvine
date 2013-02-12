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

def _find_mpi_binding():
    import use_mpi4py as mod
    if mod.world:
        return mod
    import use_pyre as mod
    if mod.world:
        return mod
    return

b = _find_mpi_binding()
if b:
    names = ['size', 'rank', 'world', 'send', 'receive']
    for name in names:
        exp = '%s = b.%s' % (name, name)
        exec exp
        continue


# version
__id__ = "$Id$"

# End of file 
