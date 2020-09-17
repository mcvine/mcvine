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

class CoherentInelastic_SingleXtal_Kernel(base):


    def __init__(self, dispersion):
        base.__init__(self, dispersion)
        return
    

    def identify(self, visitor):
        return visitor.onPhonon_CoherentInelastic_SingleXtal_Kernel(self)
    

    pass # end of CoherentInelastic_SingleXtal_Kernel


# version
__id__ = "$Id$"

# End of file 
