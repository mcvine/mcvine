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


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class IsotropicKernel(Kernel):

    '''a kernel that scatters isotropically and elastically
    '''

    def __init__(self,
                 absorption_coefficient = None,
                 scattering_coefficient = None,
                 ):
        '''new IsotropicKernel
  Inputs:
    absorption_coefficient scattering_coefficient
    '''
        self.absorption_coefficient = absorption_coefficient
        self.scattering_coefficient = scattering_coefficient
        return
        
    def identify(self, visitor): return visitor.onIsotropicKernel(self)
    
    pass



# version
__id__ = "$Id$"

# End of file 
