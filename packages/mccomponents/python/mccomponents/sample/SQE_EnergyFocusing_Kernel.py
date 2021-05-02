#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class SQE_EnergyFocusing_Kernel(Kernel):

    def __init__(
            self,
            absorption_cross_section = None,
            scattering_cross_section = None,
            unitcell_vol = None,
            SQE = None, Qrange = None, Erange = None,
            Ef = None, dEf = None,
    ):
        '''new S(Q,E) kernel

        Parameters
        ----------

        absorption_cross_section, scattering_cross_section: floats
            cross sections
        unitcell_vol: float
            unitcell volume
        SQE: functor
            S(Q,E) functor
        Qrange: 2-tuple (float)
            Q range (min, max)
        Erange: 2-tuple (float)
            E range (min, max)
        Ef, dEf: energy focusing parameters
        '''
        self.absorption_cross_section = absorption_cross_section
        self.scattering_cross_section = scattering_cross_section
        self.unitcell_vol = unitcell_vol
        self.SQE = SQE
        self.Qrange = Qrange; self.Erange = Erange
        self.Ef, self.dEf = Ef, dEf
        return

    def identify(self, visitor): return visitor.onSQE_EnergyFocusing_Kernel(self)
    pass

# End of file 
