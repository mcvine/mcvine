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


from .AbstractSANSKernel import AbstractSANSKernel as base

class SANSSphereModelKernel(base):


    def __init__(self, scale, radius, contrast, background,
                 absorption_cross_section, scattering_cross_section,
                 Qmin, Qmax):
        self.scale = scale
        self.radius = radius
        self.contrast = contrast
        self.background = background

        self.absorption_cross_section = absorption_cross_section
        self.scattering_cross_section = scattering_cross_section
        self.Qmin = Qmin
        self.Qmax = Qmax
        return

    
    def identify(self, visitor):
        return visitor.onSANSSphereModelKernel( self )


# version
__id__ = "$Id$"

# End of file 
