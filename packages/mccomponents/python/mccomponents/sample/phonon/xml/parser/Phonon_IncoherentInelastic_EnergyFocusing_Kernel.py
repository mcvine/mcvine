#!/usr/bin/env python
#


from .KernelNode import KernelNode as base


class Phonon_IncoherentInelastic_EnergyFocusing_Kernel(base):


    tag = "Phonon_IncoherentInelastic_EnergyFocusing_Kernel"
    
    
    def createKernel( self, **kwds ):
        def getval(key):
            v = kwds.get(key)
            if v: return self._parse(v)
            return v
        kargs = dict(
            Ef = getval('Ef'),
            dEf = getval('dEf'),
            average_mass = getval('average_mass'),
            scattering_xs = getval('scattering_xs'),
            absorption_xs = getval('absorption_xs'),
            )
        from mccomponents.sample.phonon \
             import incoherentinelastic_energyfocusing_kernel as f
        return f(None, **kargs)
    

    def onDOS(self, dos):
        self.element.dos = dos
        return

    onLinearlyInterpolatedDOS = onDOS


    pass # end of Phonon_IncoherentInelastic_EnergyFocusing_Kernel


from .HomogeneousScatterer import HomogeneousScatterer
HomogeneousScatterer.onPhonon_IncoherentInelastic_EnergyFocusing_Kernel = HomogeneousScatterer.onKernel


# End of file 
