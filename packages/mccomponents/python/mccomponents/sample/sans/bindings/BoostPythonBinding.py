#!/usr/bin/env python
#
#

from mccomponents.homogeneous_scatterer.bindings.BoostPythonBinding \
     import BoostPythonBinding, extend

import mccomponents.mccomponentsbp as b
import mccomposite.mccompositebp as b1
import mcni.mcnibp as b2

import numpy as np
try:
    from danse.ins import numpyext
except ImportError:
    import numpyext
    import warnings
    warnings.warn("Using old numpyext. Should use danse.ins.numpyext")

try:
    from danse.ins import bpext
except ImportError:
    import bpext
    import warnings
    warnings.warn("Using old bpext. Should use danse.ins.bpext")


class New:

    def sans_spheres_kernel(self, abs_coeff, R, phi, delta_rho, max_angle):
        """create SANS spheres kernel

        Parameters
        ----------
        absoprtion_coefficient: float. 1/m
        R: float. AA
        phi: float. 1
        delta_rho: float. fm/AA^3
        max_angle: float. degree
        """
        return b.SANSSpheresKernel(abs_coeff, R, phi, delta_rho, max_angle)

    pass # end of BoostPythonBinding


extend( New )

# End of file
