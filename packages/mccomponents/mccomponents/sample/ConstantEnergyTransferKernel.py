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
                 absorption_cross_section = None,
                 scattering_cross_section = None,
                 ):
        '''new ConstantEnergyTransferKernel
  Inputs:
    E: energy transfer
    absorption_cross_section, scattering_cross_section: cross sections
    '''
        self.E = E
        self.absorption_cross_section = absorption_cross_section
        self.scattering_cross_section = scattering_cross_section
        return
        
    def identify(self, visitor): return visitor.onConstantEnergyTransferKernel(self)
    
    pass



# version
__id__ = "$Id$"

# End of file 
