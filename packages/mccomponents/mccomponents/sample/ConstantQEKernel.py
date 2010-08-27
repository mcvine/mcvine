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
class ConstantQEKernel(Kernel):

    '''a kernel that scatters isotropically with a fixed momentum and energy transfer
    '''

    def __init__(self, 
                 Q = None,
                 E = None,
                 absorption_cross_section = None,
                 scattering_cross_section = None,
                 ):
        '''new ConstantQEKernel
  Inputs:
    Q: momentum transfer
    E: energy transfer
    absorption_cross_section, scattering_cross_section: cross sections
    '''
        self.Q = Q
        self.E = E
        self.absorption_cross_section = absorption_cross_section
        self.scattering_cross_section = scattering_cross_section
        return
        
    def identify(self, visitor): return visitor.onConstantQEKernel(self)
    
    pass



# version
__id__ = "$Id$"

# End of file 
