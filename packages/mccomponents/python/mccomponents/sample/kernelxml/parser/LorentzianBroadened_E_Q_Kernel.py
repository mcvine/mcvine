#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from .KernelNode import KernelNode as base, debug


class LorentzianBroadened_E_Q_Kernel(base):


    tag = "LorentzianBroadened_E_Q_Kernel"

    def createKernel( self, **kwds ):
        from mccomponents.sample import lorentzianbroadened_E_Q_Kernel
        # E_Q = self._parse( kwds['E_Q'] )
        # S_Q = self._parse( kwds['S_Q'] )
        E_Q = str(kwds['E_Q'])
        S_Q = str(kwds['S_Q'])
        gamma_Q = str(kwds['gamma_Q'])
        Qmin = self._parse( kwds['Qmin'] )
        Qmax = self._parse( kwds['Qmax'] )

        absorption_coefficient = kwds.get('absorption_coefficient')
        if absorption_coefficient:
            absorption_coefficient = self._parse(absorption_coefficient)

        scattering_coefficient = kwds.get('scattering_coefficient')
        if scattering_coefficient:
            scattering_coefficient = self._parse(scattering_coefficient)
        return lorentzianbroadened_E_Q_Kernel(
            E_Q=E_Q, S_Q=S_Q, gamma_Q=gamma_Q, Qmin=Qmin, Qmax=Qmax,
            absorption_coefficient = absorption_coefficient,
            scattering_coefficient = scattering_coefficient,
            )

    pass # end of E_Q_Kernel


# End of file
