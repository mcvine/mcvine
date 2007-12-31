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


def kernelEngine( kernel, binding = None ):
    "render the c++ engine of the given kernel"
    if binding is None:
        from bindings.BoostPythonBinding import BoostPythonBinding
        binding = BoostPythonBinding()
        pass

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
