#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .AbstractPhononKernel import AbstractPhononKernel as base

from . import units
meV = units.energy.meV
angstrom = units.length.angstrom


class MultiPhonon_Kernel(base):
    
    def __init__(
        self,
        dos=None,
        Qmax=None, dQ=None, Emax=None,
        scattering_xs = None, absorption_xs = None,
        average_mass = None,
        Nmax = None,
        ):
        base.__init__(self, dispersion=None)
        self.dos = dos
        self.Qmax = Qmax; self.dQ = dQ
        self.Emax = Emax
        self.average_mass = average_mass
        self.scattering_xs = scattering_xs
        self.absorption_xs = absorption_xs
        self.Nmax = Nmax or 8
        return
    
    
    def identify(self, visitor):
        return visitor.onMultiPhonon_Kernel(self)
    
    
    pass # end of MultiPhonon_Kernel


# version
__id__ = "$Id$"

# End of file 
