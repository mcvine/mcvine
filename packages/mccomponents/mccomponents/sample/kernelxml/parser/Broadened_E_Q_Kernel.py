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


from AbstractNode import AbstractNode, debug


class Broadened_E_Q_Kernel(AbstractNode):


    tag = "Broadened_E_Q_Kernel"

    def elementFactory( self, **kwds ):
        from mccomponents.sample import broadened_E_Q_Kernel
        # E_Q = self._parse( kwds['E_Q'] )
        # S_Q = self._parse( kwds['S_Q'] )
        E_Q = str(kwds['E_Q'])
        S_Q = str(kwds['S_Q'])
        sigma_Q = str(kwds['sigma_Q'])
        Qmin = self._parse( kwds['Qmin'] )
        Qmax = self._parse( kwds['Qmax'] )

        absorption_coefficient = kwds.get('absorption_coefficient')
        if absorption_coefficient:
            absorption_coefficient = self._parse(absorption_coefficient)

        scattering_coefficient = kwds.get('scattering_coefficient')
        if scattering_coefficient:
            scattering_coefficient = self._parse(scattering_coefficient)
            
        return broadened_E_Q_Kernel(
            E_Q=E_Q, S_Q=S_Q, sigma_Q=sigma_Q, Qmin=Qmin, Qmax=Qmax
            absorption_coefficient = absorption_coefficient,
            scattering_coefficient = scattering_coefficient,
            )
    
    
    pass # end of E_Q_Kernel


# version
__id__ = "$Id: E_Q_Kernel.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
