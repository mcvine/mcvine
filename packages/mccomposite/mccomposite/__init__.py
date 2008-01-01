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
    from CompositeScatterer import CompositeScatterer
    return CompositeScatterer( *args )



def scattererEngine( scatterer,
                     binding = "BoostPythonBinding",
                     orientation_convention = "McStasConvention" ):
    "render the c++ engine of the given scatterer"
    
    from bindings import classes as bindingClasses
    bindingClass = bindingClasses()[ binding ]
    binding = bindingClass()

    from orientation_conventions import classes
    conventionClass = classes()[ orientation_convention ]
    orientation_convention = conventionClass()

    from ScattererComputingEngineFactory import ScattererComputingEngineFactory
    factory = ScattererComputingEngineFactory( binding, orientation_convention )
    from ComputingEngineConstructor import ComputingEngineConstructor
    return ComputingEngineConstructor( factory ).render( scatterer )



def register( newtype, ctor_handler, binding_handlers):
    """register a new scatterer type

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
    import mcni
    import mccompositebp
    return

_import_bindings()



# version
__id__ = "$Id$"

#  End of file 
