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


import numpy as np
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
    
    from mccomponents.sample.phonon.bindings import get
    binding = get('BoostPython')
    eps_arr = binding.ndarray( eps_data )
    E_arr = binding.ndarray( E_data )
    
    # obtain min and max and store in vector_double
    E_view = E_data.view(); E_view.shape = -1, E_data.shape[-1]
    Emin = np.min(E_view, axis=0); Emax = np.max(E_view, axis=0)
    v_Emin = binding.vector_double(0); v_Emax = binding.vector_double(0)
    v_Emin.extend(Emin); v_Emax.extend(Emax)
    disp = mccomponentsbp.LinearlyInterpolatedDispersionOnGrid_3D_dblarrays(
        nAtoms, Qx_axis, Qy_axis, Qz_axis, eps_arr, E_arr, v_Emin, v_Emax )
    return disp

    
# version
__id__ = "$Id$"

# End of file 
