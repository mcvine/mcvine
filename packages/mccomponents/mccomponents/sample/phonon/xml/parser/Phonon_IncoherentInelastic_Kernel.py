#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractNode import AbstractNode, debug


class Phonon_IncoherentInelastic_Kernel(AbstractNode):


    tag = "Phonon_IncoherentInelastic_Kernel"
    

    def elementFactory( self, **kwds ):
        def getval(key):
            v = kwds.get(key)
            if v: return self._parse(v)
            return v
        kargs = dict(
            average_mass = getval('average_mass'),
            scattering_xs = getval('scattering_xs'),
            absorption_xs = getval('absorption_xs'),
            )
        from mccomponents.sample.phonon \
             import incoherentinelastic_kernel as f
        return f(None, **kargs)
    

    def onDOS(self, dos):
        self.element.dos = dos
        return

    onLinearlyInterpolatedDOS = onDOS


    pass # end of Phonon_IncoherentInelastic_Kernel


from HomogeneousScatterer import HomogeneousScatterer
HomogeneousScatterer.onPhonon_IncoherentInelastic_Kernel = HomogeneousScatterer.onKernel


# version
__id__ = "$Id: Phonon_IncoherentInelastic_Kernel.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
