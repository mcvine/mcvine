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


class IncoherentElastic_Kernel(base):

    def __init__(
        self, dw_core,
        scattering_xs = 0., absorption_xs = 0.,
        ):
        base.__init__(self, dispersion=None)
        self.dw_core = dw_core
        self.scattering_xs = scattering_xs
        self.absorption_xs = absorption_xs
        return
    

    def identify(self, visitor):
        return visitor.onPhonon_IncoherentElastic_Kernel(self)
    

    pass # end of IncoherentElastic_Kernel


# version
__id__ = "$Id: IncoherentElastic_Kernel.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
