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



from default import ComponentInterface as base

class ComponentInterface(base):

    def _get_histogram(self):
        return get_histogram(self)
    
    
def get_histogram( monitor ):
    from mcstas2.utils.carray import bpptr2npyarr
    core = monitor.core()

    nQ = core.nQ; nE =core.nE
    n = nQ * nE
    shape = nQ, nE

    Iarr = bpptr2npyarr( core.getIQE_p( ), 'double', n ).copy()
    E2arr = bpptr2npyarr( core.getIQE_p2( ), 'double', n ).copy()
    Iarr.shape = E2arr.shape = shape

    from histogram import histogram, axis, arange
    dE = (core.Emax-core.Emin)/nE
    Eaxis = axis( 'energy', arange( core.Emin, core.Emax, dE ), unit = 'meV' )

    dQ = (core.Qmax-core.Qmin)/nQ
    Qaxis = axis( 'Q', arange( core.Qmin, core.Qmax, dQ ), unit = 'angstrom**-1' )

    h = histogram( 'I(Q,E)', [Qaxis,Eaxis], data = Iarr, errors = E2arr )
    return h


# version
__id__ = "$Id$"

# End of file 
