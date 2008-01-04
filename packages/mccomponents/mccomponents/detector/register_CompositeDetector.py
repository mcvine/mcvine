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


# the interface
from mccomposite.CompositeScatterer import CompositeScatterer as base
class CompositeDetector(base):
    def identify(self, visitor): return visitor.onCompositeDetector(self)
    pass


# 2. the handler to construct c++ engine
def onCompositeDetector(self, composite):
    factory = self.factory

    elements = composite.elements()
    geometer = composite.geometer

    cscatterers = factory.scatterercontainer()
    cgeometer = factory.geometer( )
    for element in elements:
        
        self._indexes_in_detsys.append( element.id() )
        cscatterer = element.identify(self)
        self._indexes_in_detsys.pop()
        
        cscatterers.append( cscatterer )
        cposition = factory.position( geometer.position(element) )
        corientation = factory.orientation( geometer.orientation(element) )
        cgeometer.register( cscatterer, cposition, corientation )
        continue

    cshape = composite.shape().identify(self)

    return factory.compositescatterer( cshape, cscatterers, cgeometer )


# 4. register the new class and handlers
import mccomponents.homogeneous_scatterer as mh
mh.register_engine_ctor (CompositeDetector, onCompositeDetector )


# version
__id__ = "$Id$"

# End of file 
