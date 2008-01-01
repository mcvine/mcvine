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


import mccomposite.mccompositebp as binding


from AbstractBinding import AbstractBinding as base

class BoostPythonBinding(base):

    '''factory class of boost python computing engine of scatterers
    '''

    def compositescatterer(self, shape, elements, geometer):
        return binding.CompositeNeutronScatterer( shape, elements, geometer )


    def scatterercontainer(self):
        return binding.pointer_vector_NeutronScatterer( 0 )


    def shapecontainer(self):
        return binding.pointer_vector_Shape( 0 )


    def geometer(self):
        return binding.Geometer_NeutronScatterer( )


    def position(self, vector):
        return binding.Position(*vector)


    def orientation(self, rotmat):
        assert rotmat.shape == (3,3)
        rotmat1 = rotmat.copy()
        rotmat1.shape = -1,
        return binding.RotationMatrix( *rotmat1 )


    def unite(self, shapes):
        return binding.Union( shapes )

    def intersect(self, shapes):
        return binding.Intersection( shapes )

    def subtract(self, shape1, shape2):
        return binding.Difference(shape1, shape2)

    def dilate(self, shape, scale):
        return binding.Dilation( shape, scale )

    def rotate(self, shape, rotmat):
        return binding.Rotation( shape, rotmat )

    def translate(self, shape, vector):
        return binding.Translation( shape, vector )

    def block(self, diagonal):
        return binding.Block( *diagonal )

    def sphere(self, radius):
        return binding.Sphere( radius )

    def cylinder(self, radius, height):
        return binding.Cylinder( radius, height )

    pass # end of BoostPythonBinding


def register( methodname, method, override = False ):
    '''register a new handling method'''
    if hasattr(BoostPythonBinding, methodname):
        if not override:
            raise ValueError , "Cannot register handler %s. "\
                  "It was already registered." % (
                methodname )
        pass
    
    setattr( BoostPythonBinding, methodname, method )

    return


# version
__id__ = "$Id$"

# End of file 
