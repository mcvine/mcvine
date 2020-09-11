#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def composite( *args ):
    '''create a new scatterer composite
    '''
    from .CompositeScatterer import CompositeScatterer
    return CompositeScatterer( *args )


def scatterercopy( *args, **kwds ):
    '''create a copy of a scatterer
    '''
    from .ScattererCopy import ScattererCopy
    return ScattererCopy( *args, **kwds )


def scattererEngine( scatterer,
                     binding = "BoostPython",
                     orientation_convention = "McStasConvention",
                     coordinate_system = 'McStas'):
    "render the c++ engine of the given scatterer"
    
    from .bindings import get as getBinding
    binding = getBinding( binding )

    from .orientation_conventions import get
    orientation_convention = get( orientation_convention )

    from .coordinate_systems import computationEngineRenderAdpator
    Adaptor = computationEngineRenderAdpator( coordinate_system )

    from .ScattererComputationEngineFactory import ScattererComputationEngineFactory
    factory = ScattererComputationEngineFactory( binding, orientation_convention )
    from .ScattererComputationEngineRenderer import ScattererComputationEngineRenderer
    class R(Adaptor, ScattererComputationEngineRenderer): pass
    return R( factory ).render( scatterer )



def register( newtype, renderer_handler, binding_handlers, override = False):
    """register a new scatterer type

    renderer_handler will be attached to ScattererComputationEngineRenderer
    binding_handlers will be attached to corresponding classes in 'bindings'
      subpackage.
    """
    register_engine_renderer_handler( newtype, renderer_handler, override = override )
    register_binding_handlers( newtype, binding_handlers, override = override )
    return


def register_engine_renderer_handler( newtype, renderer_handler, override = False):
    """register a new scatterer type and its engine renderer handler
    """
    from . import ScattererComputationEngineRenderer
    ScattererComputationEngineRenderer.register(newtype, renderer_handler, override = override )
    return


def register_binding_handlers( newtype, binding_handlers, override = False):
    from . import bindings
    bindings.register( newtype.__name__.lower(), binding_handlers, override = override )
    return



# version
__id__ = "$Id$"

#  End of file 
