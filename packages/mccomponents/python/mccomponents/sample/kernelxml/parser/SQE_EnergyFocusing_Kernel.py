#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

from .KernelNode import KernelNode as base


class SQE_EnergyFocusing_Kernel(base):

    tag = "SQE_EnergyFocusing_Kernel"

    def createKernel( self, **kwds ):
        absorption_cross_section = kwds.get('absorption_cross_section')
        if absorption_cross_section:
            absorption_cross_section = self._parse(absorption_cross_section)
        scattering_cross_section = kwds.get('scattering_cross_section')
        if scattering_cross_section:
            scattering_cross_section = self._parse(scattering_cross_section)
        Qrange = self._parse( kwds['Q-range'] )
        Erange = self._parse( kwds['energy-range'] )
        Ef = self._parse( kwds['Ef'] )
        dEf = self._parse( kwds['dEf'] )

        from mccomponents.sample import sqe_energyfocusing_kernel as ctor
        return ctor(
            Qrange = Qrange, Erange = Erange,
            Ef = Ef, dEf = dEf,
            absorption_cross_section = absorption_cross_section,
            scattering_cross_section = scattering_cross_section,
        )


    def onSQE(self, sqe):
        self.element.SQE = sqe
        return

    onSQE_fromexpression = onGridSQE = onSQE

    pass # end of SQE_EnergyFocusing_Kernel

# End of file 
