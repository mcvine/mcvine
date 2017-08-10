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
                 Qaxes, eps_npyarr, E_npyarr,
                 dos = None):
        '''
    natoms: number of atoms in the unit cell
    dimension: 
    Qaxes: a tuple of Q axes. Each item is a 2-tuple of (q, n).
      q vector is the direction of the Q axis.
      n is the number of points along this Q axis. 
      Example: [ ( (2.2,0,0), 20), ((0,3.1,0), 20), ((0,0,1.4), 20) ] for a 3d dispersion
    eps_npyarr: numpy array of poloarization. shape  must be (3d case)
      nQx, nQy, nQz, nBranches, nAtoms, 3, 2 
    E_npyarr: numpy array of phonon energy. shape  must be (3d case)
      nQx, nQy, nQz, nBranches
      dos: a 2-tuple of E,Z
    '''
        base.__init__(self, nAtoms, dimension)
        assert len(Qaxes) == dimension
        self.Qaxes = Qaxes
        self.eps_npyarr = eps_npyarr
        self.E_npyarr = E_npyarr
        from histogram import histogram
        if dos:
            e,Z = dos
            from .utils import nice_dos
            e, Z = nice_dos(e, Z, force_fitparabolic=True)
            self.dos = histogram( 'dos', [ ('energy', e, 'meV') ], data = Z )
            pass
        return


    def identify(self, visitor):
        return visitor.onLinearlyInterpolatedDispersionOnGrid( self )

    pass # end of AbstractDispersion
    


# version
__id__ = "$Id$"

# End of file 
