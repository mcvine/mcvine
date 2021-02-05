#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

from .KernelNode import KernelNode as base, debug


class SQE_EnergyFocusing_Kernel(base):

    tag = "SQE_EnergyFocusing_Kernel"

    def createKernel( self, **kwds ):
        Qrange = self._parse( kwds['Q-range'] )
        Erange = self._parse( kwds['energy-range'] )
        Ef = self._parse( kwds['Ef'] )
        dEf = self._parse( kwds['dEf'] )

        from mccomponents.sample import sqe_energyfocusing_kernel as ctor
        return ctor(
            Qrange = Qrange, Erange = Erange,
            Ef = Ef, dEf = dEf,
        )


    def onSQE(self, sqe):
        self.element.SQE = sqe
        return

    onSQE_fromexpression = onGridSQE = onSQE

    pass # end of SQE_EnergyFocusing_Kernel

# End of file 
