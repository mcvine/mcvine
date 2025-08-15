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


from .KernelNode import KernelNode as base


class SANSSphereModelKernel(base):


    tag = "SANSSphereModelKernel"


    def createKernel( self, **kwds ):
        scale = kwds.get('scale')
        radius = kwds.get('radius')
        contrast = kwds.get('contrast')
        background = kwds.get('background')

        scale = float(scale)
        radius = float(radius)
        contrast = float(contrast)
        background = float(background)
        
        absorption_cross_section = kwds.get('absorption_cross_section')
        scattering_cross_section = kwds.get('scattering_cross_section')
        Qmin = kwds.get('Qmin')
        Qmax = kwds.get('Qmax')

        absorption_cross_section = float( absorption_cross_section )
        scattering_cross_section = float( scattering_cross_section )
        Qmin = float( Qmin )
        Qmax = float( Qmax )
        
        from mccomponents.sample.sansmodel import sansspheremodel_kernel
        return sansspheremodel_kernel(
            scale, radius, contrast, background,
            absorption_cross_section, scattering_cross_section,
            Qmin, Qmax)

    pass # end of SANSSphereModelKernel


# version
__id__ = "$Id$"

# End of file 
