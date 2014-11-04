#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2014  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class ConstantvQEKernel(Kernel):

    '''a kernel that scatters isotropically with a fixed momentum and energy transfer
    '''

    def __init__(
        self, 
        Q = None, # 3-element vector
        E = None, dE = None,
        absorption_coefficient = None,
        scattering_coefficient = None,
        ):
        '''new ConstantvQEKernel
  Inputs:
    Q: momentum transfer
    E: energy transfer
    dE: broadening allow for E
    absorption_coefficient, scattering_coefficient: cross sections
    '''
        self.Q = Q
        self.E = E
        self.dE = dE
        self.absorption_coefficient = absorption_coefficient
        self.scattering_coefficient = scattering_coefficient
        return
        
    def identify(self, visitor): return visitor.onConstantvQEKernel(self)
    
    pass



# version
__id__ = "$Id$"

# End of file 
