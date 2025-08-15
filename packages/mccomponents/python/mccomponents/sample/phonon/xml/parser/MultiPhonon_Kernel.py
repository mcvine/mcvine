#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C) 2007-2013  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .KernelNode import KernelNode as base


class MultiPhonon_Kernel(base):


    tag = "MultiPhonon_Kernel"
    

    def createKernel( self, **kwds ):
        def getval(key):
            v = kwds.get(key)
            if v: return self._parse(v)
            return v
        Nmax = kwds.get('Nmax')
        if Nmax: Nmax = int(Nmax)
        kargs = dict(
            Qmax = getval('Qmax'),
            dQ = getval('dQ'),
            Emax = getval('Emax'),
            average_mass = getval('average_mass'),
            scattering_xs = getval('scattering_xs'),
            absorption_xs = getval('absorption_xs'),
            Nmax = Nmax,
            )
        from mccomponents.sample.phonon \
             import multiphonon_kernel as f
        return f(**kargs)
    

    def onDOS(self, dos):
        self.element.dos = dos
        return

    onLinearlyInterpolatedDOS = onDOS

    pass # end of MultiPhonon_Kernel


from .HomogeneousScatterer import HomogeneousScatterer
HomogeneousScatterer.onMultiPhonon_Kernel = HomogeneousScatterer.onKernel


# version
__id__ = "$Id: Phonon_IncoherentInelastic_Kernel.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
