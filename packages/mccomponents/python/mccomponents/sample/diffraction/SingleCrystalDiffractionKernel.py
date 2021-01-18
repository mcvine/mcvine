#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

from mccomponents.homogeneous_scatterer.Kernel import Kernel
class SingleCrystalDiffractionKernel(Kernel):

    '''single crystal diffraction kernel
    '''

    def __init__(self, basis_vectors, hkllist, mosaic, Dd_over_d, abs_xs):
        '''new SingleCrystalDiffractionKernel

    Parameters
    ----------
    basis_vectors : list of 3-vectors
        basis vectors
    hkllist : list of (h,k,l,F^2)
        list of miller indices and F^2 (unit: fm^2)
    mosaic : float
        unit: radian
    Dd_over_d : float
        relative line width Delta_d/d
    abs_xs : float
        unit: barn
    '''
        self.basis_vectors = basis_vectors
        self.hkllist = hkllist
        self.mosaic = mosaic
        self.Dd_over_d = Dd_over_d
        self.abs_xs = abs_xs
        return

    def identify(self, visitor):
        return visitor.onSingleCrystalDiffractionKernel(self)
    pass

# End of file
