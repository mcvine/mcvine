#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class E_Q_Kernel(Kernel):

    '''S(Q,E) = S(Q) * delta(E-E(Q))
    '''

    def __init__(self, 
                 E_Q = None,
                 S_Q = None,
                 Qmin = None, Qmax = None,
                 absorption_coefficient = None,
                 scattering_coefficient = None,
                 ):
        '''new E_Q kernel
  Inputs:
    E_Q: E(Q) function. str
    S_Q: S(Q) function. str
    Qmin, Qmax: Q range. should have units attached. usually angstrom**-1
    absorption_coefficient, scattering_coefficient. should have units attached. usually m*-1
    '''
        self.E_Q = E_Q
        self.S_Q = S_Q
        self.Qmin = Qmin
        self.Qmax = Qmax
        self.absorption_coefficient = absorption_coefficient
        self.scattering_coefficient = scattering_coefficient
        return
        
    def identify(self, visitor): return visitor.onE_Q_Kernel(self)
    
    pass



# version
__id__ = "$Id$"

# End of file 
