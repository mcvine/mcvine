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


from mccomposite import mccompositebp
from mcni import mcnibp
class _BindingProxy:
    # when duplicated registration is avoided (see mccompositebpmodule/wrap_basics.cc)
    # symbols may be missing from mccompositebp.
    # this is a proxy to allow fallback to mcnibp if needed
    def __getattr__(self, key):
        if hasattr(mccompositebp, key): return getattr(mccompositebp, key)
        if key is "Vector":
            key = "Vector3_double"
        elif key is "RotationMatrix":
            key = "RotationMatrix_double"
        return getattr(mcnibp, key)
binding = _BindingProxy()

from AbstractBinding import AbstractBinding as Interface
from mcni.bindings.boostpython import Binding as base

class BoostPythonBinding(base, Interface):

    '''factory class of boost python computing engine of scatterers
    '''

    def compositescatterer(
        self, shape, elements, geometer,
        max_multiplescattering_loops_among_scatterers = 5,
        max_multiplescattering_loops_interactM_path1 = 2,
        min_neutron_probability = 0,
        ):
        cns = binding.CompositeNeutronScatterer( shape, elements, geometer )
        cns.max_multiplescattering_loops_among_scatterers = max_multiplescattering_loops_among_scatterers
        cns.max_multiplescattering_loops_interactM_path1 = max_multiplescattering_loops_interactM_path1
        cns.min_neutron_probability = min_neutron_probability
        return cns


    def scatterercontainer(self):
        return binding.pointer_vector_NeutronScatterer( 0 )


    def shapecontainer(self):
        return binding.pointer_vector_Shape( 0 )


    def geometer(self):
        return binding.Geometer_NeutronScatterer( )


    #def position(self, vector):
    #return binding.Position(*vector)


    def orientation(self, rotmat):
        assert rotmat.shape == (3,3)
        rotmat1 = rotmat.copy()
        rotmat1.shape = -1,
        return binding.RotationMatrix( *rotmat1 )
    

    def locate(self, position, shape):
        global _location
        return _location[binding.locate( position, shape )]
    

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

    def pyramid(self, thickness, width, height):
        return binding.Pyramid( thickness, width, height )

    def cone(self, radius, height):
        return binding.Cone( radius, height )

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


_location = None
def _init_location( ):
    global _location
    _location = {
        binding.location.inside: "inside",
        binding.location.onborder: "onborder",
        binding.location.outside: "outside",
        }

    return
    
_init_location()




# version
__id__ = "$Id$"

# End of file 
