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


class ComputationEngineRendererExtension:


    def onSANSSphereModelKernel(self, kernel):
        '''handler to create c++ instance of sans sphere model kernel
        '''
        scale = kernel.scale
        radius = kernel.radius
        contrast = kernel.contrast
        background = kernel.background
        absorption_cross_section = kernel.absorption_cross_section
        scattering_cross_section = kernel.scattering_cross_section
        Qmin = kernel.Qmin
        Qmax = kernel.Qmax
        
        return self.factory.sansspheremodel_kernel(
            scale, radius, contrast, background,
            absorption_cross_section, scattering_cross_section,
            Qmin, Qmax)


    pass # end of ComputationEngineRendererExtension



def register( type, renderer_handler_method, override = False ):
    '''register computing engine constructor method for a new type'''

    Renderer = ComputationEngineRendererExtension
    global _registry

    name = type.__name__
    methodname = 'on%s' % name
    if hasattr(Renderer, methodname):
        if not override:
            raise ValueError("Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                type, methodname, _registry[name] ))
        pass
    
    setattr( Renderer, methodname, renderer_handler_method )

    _registry[ name ] = type
    return
_registry = {}



from mccomponents.homogeneous_scatterer import registerRendererExtension
registerRendererExtension( ComputationEngineRendererExtension )


from . import units


# version
__id__ = "$Id$"

# End of file 
