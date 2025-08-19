#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C) 2006-2013  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .KernelNode import KernelNode as base


class E_vQ_Kernel(base):
    
    
    tag = "E_vQ_Kernel"
    
    def createKernel( self, **kwds ):
        from mccomponents import sample
        E_Q = str(kwds['E_Q'])
        S_Q = str(kwds['S_Q'])
        Emax = self._parse( kwds['Emax'] )
        
        absorption_coefficient = kwds.get('absorption_coefficient')
        if absorption_coefficient:
            absorption_coefficient = self._parse(absorption_coefficient)

        scattering_coefficient = kwds.get('scattering_coefficient')
        if scattering_coefficient:
            scattering_coefficient = self._parse(scattering_coefficient)
            
        return sample.make_E_vQ_Kernel(
            E_Q=E_Q, S_Q=S_Q,
            Emax = Emax,
            absorption_coefficient = absorption_coefficient,
            scattering_coefficient = scattering_coefficient,
            )
    
    
    pass # end of E_vQ_Kernel


# version
__id__ = "$Id$"

# End of file 
