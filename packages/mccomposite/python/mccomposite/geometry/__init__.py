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


from .utils import locate
from . import primitives, operations


def shapeEngine(
    shape,
    binding = "BoostPythonBinding",
    orientation_convention = "McStasConvention" ):
    
    "render the c++ engine of the given shape"
    
    from .bindings import classes as bindingClasses
    bindingClass = bindingClasses()[ binding ]
    binding = bindingClass()

    from .orientation_conventions import classes
    conventionClass = classes()[ orientation_convention ]
    orientation_convention = conventionClass()

    from .ShapeComputationEngineFactory import ShapeComputationEngineFactory
    factory = ShapeComputationEngineFactory( binding, orientation_convention )
    from .ShapeComputationEngineRenderer import ShapeComputationEngineRenderer
    return ShapeComputationEngineRenderer( factory ).render( shape )



def register( newtype, renderer_handler, binding_handlers, override = False):
    """register a new shape type

    renderer_handler will be attached to ShapeComputationEngineRenderer
    binding_handlers will be attached to corresponding classes in 'bindings'
      subpackage.
    """
    register_engine_renderer_handler( newtype, renderer_handler, override = override )
    register_binding_handlers( newtype, binding_handlers, override = override )
    return


def register_engine_renderer_handler( newtype, renderer_handler, override = False ):
    """register a new shape type and its engine renderer handler
    """
    from . import ShapeComputationEngineRenderer
    ShapeComputationEngineRenderer.register(newtype, renderer_handler, override = override)
    return


def register_binding_handlers( newtype, binding_handlers, override = False ):
    from . import bindings
    bindings.register( newtype.__name__.lower(), binding_handlers, override = override )
    return



# version
__id__ = "$Id$"

# End of file 
