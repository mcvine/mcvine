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


from AbstractVisitor import AbstractVisitor

class ComputingEngineConstructor( AbstractVisitor ):


    def __init__(self, factory):
        self.factory = factory
        return


    def render(self, scatterer):
        return scatterer.identify(self)
    

    def onCompositeScatterer(self, composite):
        factory = self.factory
        
        elements = composite.elements()
        geometer = composite.geometer
        
        cscatterers = factory.scatterercontainer()
        cgeometer = factory.geometer( )
        for element in elements:
            cscatterer = element.identify(self) 
            cscatterers.append( cscatterer )
            cposition = factory.position( geometer.position(element) )
            corientation = factory.orientation( geometer.orientation(element) )
            cgeometer.register( cscatterer, cposition, corientation )
            continue

        cshape = composite.shape().identify(self)

        return factory.compositescatterer( cshape, cscatterers, cgeometer )


    def onUnion(self, union):
        factory = self.factory
        shapes = union.shapes
        cshapes = factory.shapecontainer( )
        for shape in shapes: cshapes.append( shape.identify(self) )
        return factory.unite( cshapes )

    def onIntersection(self, intersection):
        factory = self.factory
        shapes = intersection.shapes
        cshapes = factory.shapecontainer( )
        for shape in shapes: cshapes.append( shape.identify(self) )
        return factory.intersect( cshapes )

    def onDifference(self, difference):
        factory = self.factory
        op1 = difference.op1        
        op2 = difference.op2
        cshape1 = op1.identify(self)
        cshape2 = op2.identify(self)
        return factory.subtract( cshape1, cshape2 )

    def onDilation(self, dilation):
        factory = self.factory
        body = dilation.body
        cshape = body.identify(self)
        return factory.dilate( cshape, dilation.scale)

    def onRotation(self, rotation):
        factory = self.factory
        body = rotation.body
        cshape = body.identify(self)
        rotmat = factory.orientation( rotation.angles )
        return factory.rotate( cshape, rotmat )

    def onTranslation(self, translation):
        factory = self.factory
        body = translation.body
        cshape = body.identify(self)
        offset = factory.position( translation.vector )
        return factory.translate( cshape, offset )


    def onBlock(self, block):
        diagonal = block.diagonal
        return self.factory.block( diagonal )

    def onSphere(self, sphere):
        return self.factory.sphere( sphere.radius )

    def onCylinder(self, cylinder):
        return self.factory.cylinder( cylinder.radius, cylinder.height )

    pass # end of ComputingEngineConstructor


def register( scatterer_type, constructor_visiting_method, override = False ):
    '''register computing engine constructor method for a new scatterer type'''
    name = scatterer_type.__name__
    methodname = 'on%s' % name
    if hasattr(ComputingEngineConstructor, methodname):
        if not override:
            raise ValueError , "Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                scatterer_type, methodname, _registry[name] )
        pass
    
    setattr( ComputingEngineConstructor, methodname, constructor_visiting_method )

    global _registry
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
