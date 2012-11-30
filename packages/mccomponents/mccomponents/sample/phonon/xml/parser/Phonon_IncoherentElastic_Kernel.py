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


class Phonon_IncoherentElastic_Kernel(AbstractNode):


    tag = "Phonon_IncoherentElastic_Kernel"
    

    def elementFactory( self, **kwds ):
        dw_core = self._parse( kwds['dw_core'] )
        
        from mccomponents.sample.phonon \
             import incoherentelastic_kernel as f
        return f(dw_core)
    

    pass # end of Phonon_IncoherentElastic_Kernel


from .HomogeneousScatterer import HomogeneousScatterer
HomogeneousScatterer.onPhonon_IncoherentElastic_Kernel = HomogeneousScatterer.onKernel

# version
__id__ = "$Id: Phonon_IncoherentElastic_Kernel.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
