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


def compositeKernel( *args, **kwds ):
    from CompositeKernel import CompositeKernel
    return CompositeKernel( *args, **kwds )


def homogeneousScatterer( shape, kernel, **kwds ):
    from HomogeneousScatterer import HomogeneousScatterer
    return HomogeneousScatterer(shape, kernel, **kwds)



def scattererEngine(
    scatterer,
    binding = "BoostPythonBinding",
    orientation_convention = "McStasConvention",
    coordinate_system = "McStas"):
    
    "render the c++ engine of the given scatterer"

    #the renderer class
    from mccomposite.ScattererComputationEngineRenderer import ScattererComputationEngineRenderer as Renderer1
    from KernelComputationEngineRenderer import KernelComputationEngineRenderer as Renderer2
    from mccomposite.coordinate_systems import computationEngineRenderAdpator
    Adaptor = computationEngineRenderAdpator( coordinate_system )

    class Renderer(Adaptor, Renderer1, Renderer2): pass

    #the factory class
    # 1. binding
    from mccomposite.bindings import classes
    bindingClass1 = classes() [ binding ]
    
    from bindings import classes
    bindingClass2 = classes() [ binding ]

    class B(bindingClass1, bindingClass2): pass
    binding = B()

    # 2. orientation convention
    from mccomposite.orientation_conventions import classes
    convention = classes() [orientation_convention] ()
    
    # 3. factory
    from mccomposite.ScattererComputationEngineFactory import ScattererComputationEngineFactory as S
    from KernelComputationEngineFactory import KernelComputationEngineFactory as K
    class F(S,K):
        def __init__(self, binding, orientation_convention):
            S.__init__(self, binding, orientation_convention)
            K.__init__(self, binding)
            return
        pass
    factory = F( binding,  convention )

    #render
    return Renderer( factory ).render( scatterer )


def kernelEngine( kernel, binding = "BoostPythonBinding" ):
    "render the c++ engine of the given kernel"
    from bindings import classes as bindingClasses
    binding = bindingClasses() [ binding ] ()
    
    from KernelComputationEngineFactory import KernelComputationEngineFactory
    factory = KernelComputationEngineFactory( binding )
    from KernelComputationEngineRenderer import KernelComputationEngineRenderer
    return KernelComputationEngineRenderer( factory ).render( kernel )


def register( newtype, renderer_handler, binding_handlers):
    """register a new kernel type

    renderer_handler will be attached to KernelComputationEngineRenderer
    binding_handlers will be attached to corresponding classes in 'bindings'
      subpackage.
    """
    register_engine_renderer_handler( newtype, renderer_handler )
    register_binding_handlers( newtype, binding_handlers )
    return


def register_engine_renderer_handler( newtype, renderer_handler ):
    """register a new scatterer type and its engine constructor handler
    """
    import KernelComputationEngineRenderer
    KernelComputationEngineRenderer.register(newtype, renderer_handler)
    return


def register_binding_handlers( newtype, binding_handlers ):
    import bindings
    bindings.register( newtype.__name__.lower(), binding_handlers )
    return
    

# version
__id__ = "$Id$"

# End of file 
