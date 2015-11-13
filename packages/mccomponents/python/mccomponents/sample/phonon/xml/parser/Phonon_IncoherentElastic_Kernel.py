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


from .KernelNode import KernelNode as base, debug


class Phonon_IncoherentElastic_Kernel(base):


    tag = "Phonon_IncoherentElastic_Kernel"
    

    def createKernel( self, **kwds ):
        dw_core = self._parse( kwds['dw_core'] )

        def getval(key):
            v = kwds.get(key)
            if v: return self._parse(v)
            return v
        kargs = dict(
            scattering_xs = getval('scattering_xs'),
            absorption_xs = getval('absorption_xs'),
            )
        
        from mccomponents.sample.phonon \
             import incoherentelastic_kernel as f
        return f(dw_core, **kargs)
    

    pass # end of Phonon_IncoherentElastic_Kernel


from .HomogeneousScatterer import HomogeneousScatterer
HomogeneousScatterer.onPhonon_IncoherentElastic_Kernel = HomogeneousScatterer.onKernel

# version
__id__ = "$Id: Phonon_IncoherentElastic_Kernel.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
