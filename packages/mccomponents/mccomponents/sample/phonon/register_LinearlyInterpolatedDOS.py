#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

#factory method that wraps boost python binding
def linearlyinterpolateddos(
    e0, de, n, Z):
    '''create boost python object of LinearlyInterpolatedDOS

    e0: minimum phonon energy. float
    de: phonon energy step. float
    n: number of points.
    Z: values of DOS at the energy points defined by (e0, de, n)
    '''
    import mccomponents.mccomponentsbp as b
    Z1 = b.vector_double( n )
    for i in range(n): Z1[i] = Z[i]
    
    return b.LinearlyInterpolatedDOS_dbl( e0, de, n, Z1 )



#python class to represent LinearlyInterpolatedDOS
from AbstractDOS import AbstractDOS as base
class LinearlyInterpolatedDOS(base):

    def __init__(self, doshist):
        '''doshist: a histogram instance'''
        self.doshist = doshist
        return
    
    def identify(self, visitor): return visitor.onLinearlyInterpolatedDOS( self )

    pass  # end of AbstractDOS



#register new type
# 2. the handler of engine renderer
def onLinearlyInterpolatedDOS(self, linearlyinterpolateddos):

    doshist = linearlyinterpolateddos.doshist

    eaxis = doshist.axisFromName('energy')
    if eaxis.size() < 3 :
        raise RuntimeError , "energy axis has too few bins: %s" % (
            eaxis, )
    
    energies = eaxis.binCenters()
    e0 = energies[0]
    de = energies[1] - energies[0]
    assert de>0, "energy bin should be incremental"
    
    dearr = energies[1:] - energies[:-1]
    #make sure bin sizes are all the same
    import numpy
    assert numpy.all( numpy.abs( dearr-de ) < 1e-7*de )
    n = eaxis.size()
    
    Z = doshist.data().storage().asNumarray()
    
    return self.factory.linearlyinterpolateddos(
        e0, de, n, Z )


# 3. the handler to call python bindings
def linearlyinterpolateddos_bp_handler(self, e0, de, n, Z):
    return linearlyinterpolateddos(e0, de, n, Z)


import mccomponents.homogeneous_scatterer as hs
# 4. register the new class and handlers
hs.register (
    LinearlyInterpolatedDOS, onLinearlyInterpolatedDOS,
    {'BoostPythonBinding':linearlyinterpolateddos_bp_handler} )




# version
__id__ = "$Id$"

# End of file 
