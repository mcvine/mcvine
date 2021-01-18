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


from .AbstractPhononKernel import AbstractPhononKernel as base

from . import units
meV = units.energy.meV
angstrom = units.length.angstrom

class CoherentInelastic_PolyXtal_Kernel(base):


    def __init__(self, dispersion,
                 max_omega = 55*meV
                 ):
                 # Ei = 70*meV, max_omega = 55 *meV, max_Q = 12 / angstrom,
                 # nMCsteps_to_calc_RARV = 10000,
                 # seed = None):
        base.__init__(self, dispersion)
        # self.Ei = Ei
        self.max_omega = max_omega
        # self.max_Q = max_Q
        # self.nMCsteps_to_calc_RARV = nMCsteps_to_calc_RARV
        # self.seed = seed
        return
    

    def identify(self, visitor):
        return visitor.onPhonon_CoherentInelastic_PolyXtal_Kernel(self)
    

    pass # end of CoherentInelastic_PolyXtal_Kernel


# version
__id__ = "$Id$"

# End of file 
