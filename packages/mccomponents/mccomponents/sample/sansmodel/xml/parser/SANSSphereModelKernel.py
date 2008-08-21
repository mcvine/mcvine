#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractNode import AbstractNode, debug


class SANSSphereModelKernel(AbstractNode):


    tag = "SANSSphereModelKernel"


    def elementFactory( self, **kwds ):
        scale = kwds.get('scale')
        background = kwds.get('background')
        radius = kwds.get('radius')
        contrast = kwds.get('contrast')
        
        absorption_cross_section = kwds.get('absorption_cross_section')
        scattering_cross_section = kwds.get('scattering_cross_section')
        Qmin = kwds.get('Qmin')
        Qmax = kwds.get('Qmax')
        
        from mccomponents.sample.sansmodel import sansspheremodel_kernel
        return sansspheremodel_kernel(
            scale, radius, contrast, background,
            absorption_cross_section, scattering_cross_section,
            Qmin, Qmax)

    pass # end of SANSSphereModelKernel


# version
__id__ = "$Id$"

# End of file 
