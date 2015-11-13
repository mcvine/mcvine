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


class DWFromDOS:

    def __init__(self, dos, mass, temperature, nsampling = 100):
        ''' DWFromDOS(dos, nsampling) --> a Debye Waller factor calculator based on DOS
        dos: a dos data object
        mass: mass of atoms in the unit cell
        temperature: temperature (Kelvin)
        nsampling: number of sampling point
        '''
        self.dos = dos
        self.mass = mass
        self.temperature = temperature
        self.nsampling = nsampling
        return
    
    def identify(self, visitor): return visitor.onDWFromDOS( self )

    pass  # end of DWFromDOS



# version
__id__ = "$Id$"

# End of file 
