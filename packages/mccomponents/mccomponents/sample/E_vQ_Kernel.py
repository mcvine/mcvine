#!/usr/bin/env python
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


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class E_vQ_Kernel(Kernel):

    '''S(vector Q,E) = S(vector Q) * delta(E-E(vector Q))
    '''
    
    def __init__(
        self, 
        E_Q = None,
        S_Q = None,
        Emax = None,
        absorption_coefficient = None,
        scattering_coefficient = None,
        ):
        '''new E(vector Q) kernel
  Inputs:
    E_Q: E(Qx, Qy, Qz) function. str
    S_Q: S(Qx, Qy, Qz) function. str
    Emax: maximum E transfer
    absorption_coefficient, scattering_coefficient. should have units attached. usually m*-1
    '''
        self.E_Q = E_Q
        self.S_Q = S_Q
        self.Emax = Emax
        self.absorption_coefficient = absorption_coefficient
        self.scattering_coefficient = scattering_coefficient
        return
        
    def identify(self, visitor): return visitor.onE_vQ_Kernel(self)
    
    pass



# version
__id__ = "$Id$"

# End of file 
