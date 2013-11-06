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
class ConstantEnergyTransferKernel(Kernel):

    '''a kernel that scatters isotropically with a fixed energy transfer
    '''

    def __init__(self, 
                 E = None,
                 absorption_coefficient = None,
                 scattering_coefficient = None,
                 ):
        '''new ConstantEnergyTransferKernel
  Inputs:
    E: energy transfer
    absorption_coefficient, scattering_coefficient: cross sections
    '''
        self.E = E
        self.absorption_coefficient = absorption_coefficient
        self.scattering_coefficient = scattering_coefficient
        return
        
    def identify(self, visitor): return visitor.onConstantEnergyTransferKernel(self)
    
    pass



# version
__id__ = "$Id$"

# End of file 
