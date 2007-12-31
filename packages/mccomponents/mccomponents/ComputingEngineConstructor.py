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
        return


    def render(self, target):
        return target.identify(self)
    

    def onCompositeKernel(self, composite):
        factory = self.factory
        
        elements = composite.elements()
        
        ckernels = factory.kernelcontainer()
        for element in elements:
            ckernel = element.identify(self) 
            ckernels.append( ckernel )
            continue

        return factory.composite( ckernels )

    
    def onHomogenousScatterer(self, scatterer):
        factory = self.factory

        ckernel = scatterer.kernel().identify(self)

        cshape = scatterer.shape().identify(self)

        cweights = factory.mcweights_absorption_scattering_transmission(
            scatterer.mcweights_absorption_scattering_transmission)

        return factory.homogeneousScatterer( cshape, ckernel, cweights )

    pass # end of ComputingEngineConstructor


def register( kernel_type, constructor_visiting_method, override = False ):
    '''register computing engine constructor method for a new kernel type'''
    name = kernel_type.__name__
    methodname = 'on%s' % name
    if hasattr(ComputingEngineConstructor, methodname):
        if not override:
            raise ValueError , "Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                kernel_type, methodname, _registry[name] )
        pass
    
    setattr( ComputingEngineConstructor, methodname, constructor_visiting_method )

    global _registry
    _registry[ name ] = kernel_type
    return


_registry = {}
def _init_registry():
    from CompositeKernel import CompositeKernel
    _registry['CompositeKernel'] = CompositeKernel
    from HomogeneousScatterer import HomogeneousScatterer
    _registry['HomogeneousScatterer'] = HomogeneousScatterer
    return


_init_registry()


# version
__id__ = "$Id$"

# End of file 
