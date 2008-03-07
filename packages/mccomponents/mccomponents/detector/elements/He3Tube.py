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


import units

from mccomposite.CompositeScatterer import CompositeScatterer as base

class He3Tube(base):
    
    def __init__(self, shape,
                 id = 0, pressure = units.pressure.atm,
                 mcweights = (0.9,0,0.1) ):
        
        base.__init__(self, shape)
        self._id = id
        self._pressure = pressure
        self.mcweights = mcweights
        return
    
    def id(self): return self._id
    
    def pressure(self): return self._pressure
    
    def identify(self, visitor): return visitor.onHe3Tube(self)
    
    pass


# version
__id__ = "$Id$"

# End of file 
