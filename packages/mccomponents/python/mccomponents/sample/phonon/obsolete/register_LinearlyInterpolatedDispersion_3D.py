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

#factory method that wraps boost python binding
def linearlyinterpolateddispersion_3d_bp(
    natoms, Qaxes, eps_npyarr, E_npyarr ):
    '''create boost python object of LinearlyInterpolatedDispersion_3D

    natoms: number of atoms in the unit cell
    Qaxes: a 3-tuple of Q axes. Each item is a 3-tuple of (min, step, n)
        Example: [ (-10., 1., 20), (-10., 1., 20), (-10., 1., 20) ]
    eps_npyarr: numpy array of poloarization. shape  must be
        nQx, nQy, nQz, nBranches, nAtoms, 3, 2 
    E_npyarr: numpy array of phonon energy. shape  must be
        nQx, nQy, nQz, nBranches 
    '''
    from mccomponents import mccomponentsbp
    #c++ engine require Qmax = Qmin + n * step, and that means n+1 Q points
    for i,axis in enumerate(Qaxes):
        Qaxes[i] = axis[0], axis[1], axis[2]-1
        continue
    Qx_axis = mccomponentsbp.LinearlyInterpolatableAxis_dbl( *(Qaxes[0]) )
    Qy_axis = mccomponentsbp.LinearlyInterpolatableAxis_dbl( *(Qaxes[1]) )
    Qz_axis = mccomponentsbp.LinearlyInterpolatableAxis_dbl( *(Qaxes[2]) )
    
    from register_NdArray import ndarray_bp
    eps_arr = ndarray_bp( eps_npyarr )
    E_arr = ndarray_bp( E_npyarr )

    disp = mccomponentsbp.LinearlyInterpolatedDispersionOnGrid_3D_dblarrays(
        natoms, Qx_axis, Qy_axis, Qz_axis, eps_arr, E_arr )
    return disp


# version
__id__ = "$Id$"

# End of file 
