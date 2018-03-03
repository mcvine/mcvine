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



class ShapeComputationEngineRenderer:

    '''render computation engine of a shape representation
    '''

    def __init__(
        self, factory,
        length_unit = units.length.meter,
        angle_unit = units.angle.degree ):
        
        self.factory = factory
        from units_utils import UnitsRemover
        self._unitsRemover = UnitsRemover(
            length_unit = length_unit,
            angle_unit = angle_unit,
            )
        return


    def render(self, shape):
        return shape.identify(self)
    
    #handlers

    # 1. for operations
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
        angles = self._remove_angle_unit( rotation.angles )
        rotmat = factory.orientation( angles )
        return factory.rotate( cshape, rotmat )

    def onTranslation(self, translation):
        factory = self.factory
        body = translation.body
        cshape = body.identify(self)
        vector = self._remove_length_unit( translation.vector )
        offset = factory.position( vector )
        return factory.translate( cshape, offset )


    # 2. for primitives
    def onBlock(self, block):
        diagonal = block.diagonal
        diagonal = self._remove_length_unit( diagonal )
        return self.factory.block( diagonal )

    def onSphere(self, sphere):
        r = self._remove_length_unit(sphere.radius)
        return self.factory.sphere( r )

    def onCylinder(self, cylinder):
        p = self._remove_length_unit( (cylinder.radius, cylinder.height) )
        return self.factory.cylinder( *p )

    def onPyramid(self, pyramid):
        p = self._remove_length_unit( (pyramid.thickness, pyramid.width, pyramid.height) )
        return self.factory.pyramid( *p )


    # helpers
    def _remove_length_unit(self, t):
        return self._unitsRemover.remove_length_unit( t )
    
    def _remove_angle_unit(self, t):
        return self._unitsRemover.remove_angle_unit( t )
    
    
    pass # end of ShapeComputationEngineRenderer




def register( shape_type, engine_renderer_method, override = False ):
    '''register computing engine renderer method for a new scatterer type'''

    global _registry
    
    name = shape_type.__name__
    methodname = 'on%s' % name
    if hasattr(ShapeComputationEngineRenderer, methodname):
        if not override:
            raise ValueError , "Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                shape_type, methodname, _registry[name] )
        pass
    
    setattr( ShapeComputationEngineRenderer, methodname, engine_renderer_method )

    _registry[ name ] = shape_type
    return


_registry = {}
def _init_registry():
    from operations import Union, Intersection, Difference, Dilation, Translation, Rotation
    from primitives import Block, Cylinder, Sphere, Pyramid
    for klass in Union, Intersection, Difference, Dilation, Translation, Rotation,\
            Block, Cylinder, Sphere, Pyramid:
        _registry[klass.__name__] = klass
        continue
    return


_init_registry()


# version
__id__ = "$Id$"

# End of file 
