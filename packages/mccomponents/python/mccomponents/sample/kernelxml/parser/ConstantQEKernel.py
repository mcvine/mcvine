#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .KernelNode import KernelNode as base


class ConstantQEKernel(base):


    tag = "ConstantQEKernel"

    def createKernel( self, **kwds ):
        from mccomponents.sample import constantQEKernel
        E = self._parse( kwds['energy-transfer'] )
        Q = self._parse( kwds['momentum-transfer'] )

        absorption_coefficient = kwds.get('absorption_coefficient')
        if absorption_coefficient:
            absorption_coefficient = self._parse(absorption_coefficient)
            
        scattering_coefficient = kwds.get('scattering_coefficient')
        if scattering_coefficient:
            scattering_coefficient = self._parse(scattering_coefficient)
            
        return constantQEKernel(
            Q, E, absorption_coefficient, scattering_coefficient)
    
    
    pass # end of ConstantQEKernel


# version
__id__ = "$Id$"

# End of file 
