#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp


def example():
    nQs = 25
    Qx_axis = mccomponentsbp.LinearlyInterpolatableAxis_dbl( -12, 1., nQs )
    Qy_axis = mccomponentsbp.LinearlyInterpolatableAxis_dbl( -12, 1., nQs )
    Qz_axis = mccomponentsbp.LinearlyInterpolatableAxis_dbl( -12, 1., nQs )
    nAtoms = 5
    nDims = 3
    nBranches = nAtoms*nDims
    import numpy
    eps_data = numpy.zeros(
        ( nQs+1, nQs+1, nQs+1, nBranches, nAtoms, nDims, 2 ),
        dtype = numpy.double)
    E_data = numpy.zeros(
        ( nQs+1, nQs+1, nQs+1, nBranches ),
        dtype = numpy.double)
    
    from mccomponents.sample.phonon.register_NdArray import ndarray_bp
    eps_arr = ndarray_bp( eps_data )
    E_arr = ndarray_bp( E_data )
    
    disp = mccomponentsbp.LinearlyInterpolatedDispersionOnGrid_3D_dblarrays(
        nAtoms, Qx_axis, Qy_axis, Qz_axis, eps_arr, E_arr )
    return disp

    
# version
__id__ = "$Id$"

# End of file 
