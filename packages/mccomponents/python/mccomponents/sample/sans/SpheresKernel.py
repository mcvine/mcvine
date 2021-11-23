#!/usr/bin/env python
#
#

from . import units
meV = units.energy.meV
angstrom = units.length.angstrom
sld_unit = 1e-15*units.length.m/units.length.angstrom**3
deg = units.angle.deg

from mccomponents.homogeneous_scatterer.Kernel import Kernel as base
class SpheresKernel(base):

    def __init__(self, abs_coeff=None, R=100.*angstrom, phi=1e-3, delta_rho=0.6*sld_unit, max_angle=3*deg):
        """ SpheresKernel constructor

        Parameters
        ----------
        absoprtion_coefficient: pyre unit. 1/length
        R: pyre unit. length
        phi: float. 1
        delta_rho: pyre unit. 1/length^2
        max_angle: pyre unit
        """
        self.abs_coeff = abs_coeff
        self.R = R
        self.phi = phi
        self.delta_rho = delta_rho
        self.max_angle = max_angle
        return

    def identify(self, visitor):
        return visitor.onSANSSpheresKernel(self)

    pass # end of SpheresKernel

# End of file
