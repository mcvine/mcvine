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


    def onBlock(self, block):
        diagonal = self._remove_length_unit( block.diagonal )
        return self.factory.block( diagonal )

    def onSphere(self, sphere):
        r = self._remove_length_unit(sphere.radius)
        return self.factory.sphere( r )

    def onCylinder(self, cylinder):
        p = self._remove_length_unit( (cylinder.radius, cylinder.height) )
        return self.factory.cylinder( *p )


    def onScattererCopy(self, copy):

        reference = copy.reference ()
        
        import mccomposite
        c = mccomposite.composite( reference.shape() )
        c.addElement( reference )
        
        return c.identify(self)

    def _remove_length_unit(self, t): return remove_unit( t, length_unit )
    
    def _remove_angle_unit(self, t): return remove_unit( t, angle_unit )
    
    
    def _remember(self, visitee, cobject ):
        self._memo[ visitee ] = cobject
        return

    def _get(self, visitee):
        return self._memo.get( visitee )

    pass # end of ComputingEngineConstructor


def register( scatterer_type, constructor_visiting_method, override = False ):
    '''register computing engine constructor method for a new scatterer type'''

    global _registry
    
    name = scatterer_type.__name__
    methodname = 'on%s' % name
    if hasattr(ComputingEngineConstructor, methodname):
        if not override:
            raise ValueError , "Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                scatterer_type, methodname, _registry[name] )
        pass
    
    setattr( ComputingEngineConstructor, methodname, constructor_visiting_method )

    _registry[ name ] = scatterer_type
    return


_registry = {}
def _init_registry():
    from CompositeScatterer import CompositeScatterer
    _registry['CompositeScatterer'] = CompositeScatterer
    return


_init_registry()



def is_unitless_scalar( s ):
    return isinstance(s, float) or isinstance(s, int)

def remove_unit_of_scalar( s, unit ):
    try:
        s+unit
        return s/unit
    except:
        raise ValueError, "incommpatible unit: %s, %s" % (s, unit)
    

def is_unitless_vector( v ):
    for i in v:
        if not is_unitless_scalar( i ):
            return False
        continue
    return True


def remove_unit_of_vector( v, unit ):
    from numpy import array
        
    v = array(v) * 1.0
    try:
        v[0] + unit
        #this means the v has compatible unit
        v = v/unit
    except:
        pass

    for i in v:
        if not isinstance(i, float):
            raise ValueError , "v should have unit of length: %s" %(
                v, )
        continue
    # this means v already is a unitless vector
    return v



def remove_unit( something, unit ):
    if '__iter__' in dir(something):
        if not is_unitless_vector( something ):
            return remove_unit_of_vector( something, unit)
    else:
        if not is_unitless_scalar( something ):
            return remove_unit_of_scalar( something, unit )
        pass
    return something
        


import units
length_unit = units.length.meter
angle_unit = units.angle.degree

# version
__id__ = "$Id$"

# End of file 
