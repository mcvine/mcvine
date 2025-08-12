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


class ConstantEnergyTransferKernel(base):


    tag = "ConstantEnergyTransferKernel"

    def createKernel( self, **kwds ):
        from mccomponents.sample import constantEnergyTransferKernel
        E = self._parse( kwds['energy-transfer'] )
        
        absorption_coefficient = kwds.get('absorption_coefficient')
        if absorption_coefficient:
            absorption_coefficient = self._parse(absorption_coefficient)
            
        scattering_coefficient = kwds.get('scattering_coefficient')
        if scattering_coefficient:
            scattering_coefficient = self._parse(scattering_coefficient)
            
        return constantEnergyTransferKernel(E, absorption_coefficient, scattering_coefficient)
    
    
    pass # end of ConstantEnergyTransferKernel


# version
__id__ = "$Id$"

# End of file 
