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
        from mccomponents.sample.phonon \
             import incoherentinelastic_kernel as f
        return f(None)
    

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
