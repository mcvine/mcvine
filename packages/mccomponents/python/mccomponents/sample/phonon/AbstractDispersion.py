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


class AbstractDispersion:

    def __init__(self, nAtoms, dimension):
        self.nAtoms = nAtoms
        self.dimension = dimension
        self.nBranches = nAtoms * dimension
        return


    def energy(self, branch_id, Q): raise NotImplementedError


    def polarization(self, branch_id, atom_id, Q): raise NotImplementedError
    
    
    pass # end of AbstractDispersion
    


# version
__id__ = "$Id$"

# End of file 
