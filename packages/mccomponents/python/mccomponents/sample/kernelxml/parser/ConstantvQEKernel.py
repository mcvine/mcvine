#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C) 2006-2014  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .KernelNode import KernelNode as base


class ConstantvQEKernel(base):


    tag = "ConstantvQEKernel"

    def createKernel( self, **kwds ):
        from mccomponents.sample import constantvQEKernel
        E = self._parse( kwds['energy-transfer'] )
        dE = self._parse( kwds['dE'] )
        Q = self._parse( kwds['momentum-transfer'] )
        
        absorption_coefficient = kwds.get('absorption_coefficient')
        if absorption_coefficient:
            absorption_coefficient = self._parse(absorption_coefficient)
            
        scattering_coefficient = kwds.get('scattering_coefficient')
        if scattering_coefficient:
            scattering_coefficient = self._parse(scattering_coefficient)
            
        return constantvQEKernel(
            Q, E, dE, absorption_coefficient, scattering_coefficient)
    
    
    pass # end of ConstantvQEKernel


# version
__id__ = "$Id: ConstantvQEKernel.py 1797 2014-03-21 20:02:20Z linjiao $"

# End of file 
