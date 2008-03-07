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
    coordinate_system = "McStas",
    ComputationEngineRendererExtensions = [],
    ):
    
    "render the c++ engine of the given scatterer"

    #the renderer classes
    Bases = _rendererBases( )
    
    from mccomposite.coordinate_systems import computationEngineRenderAdpator
    Adaptor = computationEngineRenderAdpator( coordinate_system )

    klasses = Bases + [Adaptor] + registeredRendererExtensions() + ComputationEngineRendererExtensions 
    klasses.reverse()

    Renderer = _inherit( klasses )

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
    """render the c++ engine of the given kernel
    
    This factory method can only deal with kernels, but not scatterers.
    """
    from bindings import classes as bindingClasses
    binding = bindingClasses() [ binding ] ()
    
    from KernelComputationEngineFactory import KernelComputationEngineFactory
    factory = KernelComputationEngineFactory( binding )
    from KernelComputationEngineRenderer import KernelComputationEngineRenderer
    return KernelComputationEngineRenderer( factory ).render( kernel )



# for extending this package in a minimal effort way.
# These methods should only be used for very simple extensions.
# For more complex extensions, you should first create the extension
# class, and then either register the extension,
# or use the extension on the fly by putting them into the
# "ComputationEngineRendererExtensions" parameter of method
# "scattererEngine".
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



#computation engine renderer

# bases
def _rendererBases():
    from mccomposite.ScattererComputationEngineRenderer import ScattererComputationEngineRenderer 
    from KernelComputationEngineRenderer import KernelComputationEngineRenderer
    return [ KernelComputationEngineRenderer, ScattererComputationEngineRenderer ]


# renderer extension registry methods
def registeredRendererExtensions():
    global _registeredRendererExtensions
    return _registeredRendererExtensions
_registeredRendererExtensions = []

def registerRendererExtension( extension_class ):
    global _registeredRendererExtensions
    _registeredRendererExtensions.append( extension_class )
    return

def removeRendererExtension( extension_class ):
    global _registeredRendererExtensions
    reg = _registeredRendererExtensions
    if extension_class in reg:
        del reg[ reg.index( extension_class ) ]
    return


#helpers
def _inherit( klasses ):
    #print klasses
    P = klasses
    code = "class _( %s ): pass" % ','.join( [ 'P[%s]' % i for i in range(len(P)) ] )
    #print code
    exec code in locals()
    return _


# version
__id__ = "$Id$"

# End of file 
