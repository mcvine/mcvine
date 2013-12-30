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

    def __init__(
        self, shape, kernel,
        mcweights = (1,1,1),
        max_multiplescattering_loops = 5,
        min_neutron_probability = 0.,
        packing_factor = 1.,
        ):
        '''create a new homogeneous scatterer
        
    shape: geometric shape
    kernel: scattering kernel
    mcweights: monte carlo weights for (absorption, scattering, transmission)
    '''
        Scatterer.__init__(self, shape)
        self._kernel = kernel
        self.mcweights = mcweights
        self.max_multiplescattering_loops = max_multiplescattering_loops
        self.min_neutron_probability = min_neutron_probability
        self.packing_factor = packing_factor
        return
    
    
    def kernel(self): return self._kernel


    def setKernel(self, kernel): self._kernel = kernel


    def identify(self, visitor): return visitor.onHomogeneousScatterer(self)


    pass # end of HomogeneousScatterer


# version
__id__ = "$Id$"

# End of file 
