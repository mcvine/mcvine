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


from AbstractPhononKernel import AbstractPhononKernel as base

import units
meV = units.energy.meV
angstrom = units.length.angstrom


class IncoherentInelastic_Kernel(base):

    def __init__(
        self,
        dos,
        ):
        base.__init__(self, dispersion=None)
        self.dos = dos
        return
    

    def identify(self, visitor):
        return visitor.onPhonon_IncoherentInelastic_Kernel(self)
    

    pass # end of IncoherentInelastic_Kernel


# version
__id__ = "$Id: IncoherentInelastic_Kernel.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
