#!/usr/bin/env python
#


from AbstractPhononKernel import AbstractPhononKernel as base

import units
meV = units.energy.meV
angstrom = units.length.angstrom


class IncoherentInelastic_EnergyFocusing_Kernel(base):

    def __init__(
        self,
        dos, Ef, dEf,
        average_mass = 0., scattering_xs = 0., absorption_xs = 0.
        ):
        """
        Ef, dEf: focusing parameter
        average_mass, scattering_xs, absorption_xs: 
            if 0, will compute from unitcell
            otherwise, must have appropriate units attached
        """
        base.__init__(self, dispersion=None)
        self.dos = dos
        self.Ef = Ef; self.dEf = dEf
        self.average_mass = average_mass
        self.scattering_xs = scattering_xs
        self.absorption_xs = absorption_xs
        return
    

    def identify(self, visitor):
        return visitor.onPhonon_IncoherentInelastic_EnergyFocusing_Kernel(self)
    

    pass # end of IncoherentInelastic_EnergyFocusing_Kernel

# End of file 
