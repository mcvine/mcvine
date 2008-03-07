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
class SQEkernel(Kernel):

    def __init__(self,
                 absorption_cross_section = None,
                 scattering_cross_section = None,
                 SQE = None, Qrange = None, Erange = None,
                 ):
        '''new S(Q,E) kernel
  Inputs:
    absorption_cross_section, scattering_cross_section: cross sections
    SQE: S(Q,E) functor
    Qrange: Q range (min, max)
    Erange: E range (min, max)
    '''
        self.absorption_cross_section = absorption_cross_section
        self.scattering_cross_section = scattering_cross_section
        self.SQE = SQE
        self.Qrange = Qrange; self.Erange = Erange
        return
        
    def identify(self, visitor): return visitor.onSQEkernel(self)
    
    pass



# version
__id__ = "$Id$"

# End of file 
