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
                 absorption_cross_section = None,
                 scattering_cross_section = None,
                 ):
        '''new IsotropicKernel
  Inputs:
    absorption_cross_section, scattering_cross_section: cross sections
    '''
        self.absorption_cross_section = absorption_cross_section
        self.scattering_cross_section = scattering_cross_section
        return
        
    def identify(self, visitor): return visitor.onIsotropicKernel(self)
    
    pass



# version
__id__ = "$Id$"

# End of file 
