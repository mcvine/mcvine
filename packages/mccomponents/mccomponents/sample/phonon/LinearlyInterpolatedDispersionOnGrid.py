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


from AbstractDispersion import AbstractDispersion as base

class LinearlyInterpolatedDispersionOnGrid(base):

    def __init__(self, nAtoms, dimension,
                 Qaxes, eps_npyarr, E_npyarr ):
        '''
    natoms: number of atoms in the unit cell
    dimension: 
    Qaxes: a tuple of Q axes. Each item is a 3-tuple of (min, step, n)
        Example: [ (-10., 1., 20), (-10., 1., 20), (-10., 1., 20) ] for 3d dispersion
        n is number of points on axis.
    eps_npyarr: numpy array of poloarization. shape  must be (3d case)
        nQx, nQy, nQz, nBranches, nAtoms, 3, 2 
    E_npyarr: numpy array of phonon energy. shape  must be (3d case)
        nQx, nQy, nQz, nBranches 
    '''
        base.__init__(self, nAtoms, dimension)
        assert len(Qaxes) == dimension
        self.Qaxes = Qaxes
        self.eps_npyarr = eps_npyarr
        self.E_npyarr = E_npyarr
        return


    def identify(self, visitor):
        return visitor.onLinearlyInterpolatedDispersionOnGrid( self )

    pass # end of AbstractDispersion
    


# version
__id__ = "$Id$"

# End of file 
