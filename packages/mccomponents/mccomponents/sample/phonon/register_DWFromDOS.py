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

#python class to represent DWFromDOS
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



#register new type
# 2. the handler of engine renderer
def onDWFromDOS(self, dwfromDOS):

    dos = dwfromDOS.dos
    cdos = dos.identify(self)

    mass = dwfromDOS.mass
    temperature = dwfromDOS.temperature

    return self.factory.dwfromDOS(
        cdos, mass, temperature, dwfromDOS.nsampling )


# 3. the handler to call python bindings
def dwfromDOS_bp_handler(self, dos, mass, temperature, nsampling):
    from mccomponents import mccomponentsbp as bp
    ret = bp.DWFromDOS_dbl(dos, nsampling)
    ret.calc_DW_core( mass, temperature )
    return ret


import mccomponents.homogeneous_scatterer as hs
# 4. register the new class and handlers
hs.register (
    DWFromDOS, onDWFromDOS,
    {'BoostPythonBinding':dwfromDOS_bp_handler} )




# version
__id__ = "$Id$"

# End of file 
