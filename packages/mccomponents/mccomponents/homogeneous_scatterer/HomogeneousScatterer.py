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


from mccomposite.Scatterer import Scatterer

class HomogeneousScatterer(Scatterer):

    def __init__(self, shape, kernel,
                 mcweights_absorption_scattering_transmission = (1,1,1)):
        '''create a new homogeneous scatterer
        
    shape: geometric shape
    kernel: scattering kernel
    mcweights_absorption_scattering_transmission: monte carlo weights for (absorption, scattering, transmission)
    '''
        Scatterer.__init__(self, shape)
        self._kernel = kernel
        self.mcweights_absorption_scattering_transmission = mcweights_absorption_scattering_transmission
        return
    
    
    def kernel(self): return self._kernel


    def identify(self, visitor): return visitor.onHomogeneousScatterer(self)
    
    
    pass # end of HomogeneousScatterer


# version
__id__ = "$Id$"

# End of file 
