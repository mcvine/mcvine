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



from AbstractVisitor import AbstractVisitor
from geometry.ShapeComputationEngineRenderer import ShapeComputationEngineRenderer


class ScattererComputationEngineRenderer( AbstractVisitor, ShapeComputationEngineRenderer ):

    '''Visitor of scatterer hierarchy. It renders computation engine
    of the scatterer hierarchy.

    This class delegates to a factory class to create instance of
    computation engine of individual scatterer.
    '''


    def __init__(
        self, factory,
        length_unit = units.length.meter,
        angle_unit = units.angle.degree ):

        ShapeComputationEngineRenderer.__init__(
            self, factory,
            length_unit = length_unit, angle_unit = angle_unit )
        
        self.factory = factory
        self._memo = {}
        return


    def render(self, scatterer):
        return scatterer.identify(self)
    

    def onCompositeScatterer(self, composite):
        ret =  self._get( composite )
        if ret: return ret
        
        factory = self.factory
        
        elements = composite.elements()
        geometer = composite.geometer
        
        cscatterers = factory.scatterercontainer()
        cgeometer = factory.geometer( )

        for element in elements:
            cscatterer = element.identify(self) 
            cscatterers.append( cscatterer )
            
            position = self._remove_length_unit( geometer.position(element) )
            cposition = factory.position( position )
            
            orientation = self._remove_angle_unit( geometer.orientation(element) )
            corientation = factory.orientation( orientation )

            cgeometer.register( cscatterer, cposition, corientation )
            continue

        cshape = composite.shape().identify(self)

        ret =  factory.compositescatterer( cshape, cscatterers, cgeometer )
        self._remember( composite, ret )
        return ret


    def onScattererCopy(self, copy):
        reference = copy.reference ()
        klass = reference.__class__.__name__
        handler = getattr( self, 'on%sCopy' % klass)
        return handler( copy )


    def onCompositeScattererCopy(self, copy):
        ref = copy.reference()
        return ref.identify(self)


    def _remember(self, visitee, cobject ):
        self._memo[ visitee ] = cobject
        return

    def _get(self, visitee):
        return self._memo.get( visitee )

    pass # end of ScattererComputationEngineRenderer


def register( scatterer_type, renderer_handler, override = False ):
    '''register computing engine renderer handler method for a new scatterer type'''

    global _registry
    
    name = scatterer_type.__name__
    methodname = 'on%s' % name
    if hasattr(ScattererComputationEngineRenderer, methodname):
        if not override:
            raise ValueError , "Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                scatterer_type, methodname, _registry[name] )
        pass
    
    setattr( ScattererComputationEngineRenderer, methodname, renderer_handler )

    _registry[ name ] = scatterer_type
    return


_registry = {}
def _init_registry():
    from CompositeScatterer import CompositeScatterer
    _registry['CompositeScatterer'] = CompositeScatterer
    return


_init_registry()




# version
__id__ = "$Id$"

# End of file 
