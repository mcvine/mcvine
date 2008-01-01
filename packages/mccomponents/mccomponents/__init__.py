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



def scattererEngine( scatterer,
                     binding = "BoostPythonBinding",
                     orientation_convention = "McStasConvention"):
    "render the c++ engine of the given scatterer"
    from mccomposite.ComputingEngineConstructor import ComputingEngineConstructor as C1
    from ComputingEngineConstructor import ComputingEngineConstructor as C2
    class C(C1, C2): pass

    from mccomposite.bindings import classes
    bindingClass1 = classes() [ binding ]
    
    from bindings import classes
    bindingClass2 = classes() [ binding ]

    class B(bindingClass1, bindingClass2): pass

    from mccomposite.ScattererComputingEngineFactory import ScattererComputingEngineFactory as S
    from KernelComputingEngineFactory import KernelComputingEngineFactory as K
    class F(S,K):
        def __init__(self, binding, orientation_convention):
            S.__init__(self, binding, orientation_convention)
            K.__init__(self, binding)
            return
        pass

    from mccomposite.orientation_conventions import classes
    convention = classes() [orientation_convention] ()
    binding = B()
    
    factory = F( binding,  convention )
    
    return C( factory ).render( scatterer )


def kernelEngine( kernel, binding = "BoostPythonBinding" ):
    "render the c++ engine of the given kernel"
    from bindings import classes as bindingClasses
    binding = bindingClasses() [ binding ] ()
    
    from KernelComputingEngineFactory import KernelComputingEngineFactory
    factory = KernelComputingEngineFactory( binding )
    from ComputingEngineConstructor import ComputingEngineConstructor
    return ComputingEngineConstructor( factory ).render( kernel )


def register( newtype, ctor_handler, binding_handlers):
    """register a new kernel type

    ctor_handler will be attached to ComputingEngineConstructor
    binding_handlers will be attached to corresponding classes in 'bindings'
      subpackage.
    """
    import ComputingEngineConstructor
    ComputingEngineConstructor.register(newtype, ctor_handler)
    import bindings
    bindings.register( newtype.__name__.lower(), binding_handlers )
    return

    

def _import_bindings():
    import mccomposite
    import mccomponentsbp
    return

_import_bindings()


# version
__id__ = "$Id$"

# End of file 
