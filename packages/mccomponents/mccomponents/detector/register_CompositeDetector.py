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
    def __init__(self, shape, id = 0):
        base.__init__(self, shape)
        self._id = id
        return
    def id(self): return self._id
    def identify(self, visitor): return visitor.onCompositeDetector(self)
    pass


# 2. the handler to construct c++ engine
def onCompositeDetector(self, composite):
    factory = self.factory

    elements = composite.elements()
    geometer = composite.geometer

    cscatterers = factory.scatterercontainer()
    cgeometer = factory.geometer( )
    for index, element in enumerate(elements):

        #index is the index of this element in its container
        #this way array indexing will be easy.
        self._indexes_in_detsys.append( index )
        cscatterer = element.identify(self)
        self._indexes_in_detsys.pop()
        
        cscatterers.append( cscatterer )

        position = self._remove_length_unit( geometer.position(element) )
        cposition = factory.position( position )
            
        orientation = self._remove_angle_unit( geometer.orientation(element) )
        corientation = factory.orientation( orientation )
            
        cgeometer.register( cscatterer, cposition, corientation )
        continue

    cshape = composite.shape().identify(self)

    return factory.compositescatterer( cshape, cscatterers, cgeometer )


# 4. register the new class and handlers
import mccomponents.homogeneous_scatterer as mh
mh.register_engine_renderer_handler (CompositeDetector, onCompositeDetector )


# version
__id__ = "$Id$"

# End of file 
