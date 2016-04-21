#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''
methods to generate seeds for random number generator
'''

def usetimer():
    return int(time.time() * 1e6) % 2**nbits_seedt

import time
nbits_seedt = 16


def usetimer_p():
    from utils.mpi import rank as mpirank
    return usetimer() + mpirank


seed = None


def use( strategy ):
    global seed
    seed = _methods.get( strategy )
    if seed is None:
        raise ValueError, "Invalid strategy: %r" % strategy
    return

_methods = {
    'timer': usetimer,
    'timer_p': usetimer_p,
    #
    'default': usetimer_p,
    }


use('default')



# version
__id__ = "$Id$"

# End of file 
