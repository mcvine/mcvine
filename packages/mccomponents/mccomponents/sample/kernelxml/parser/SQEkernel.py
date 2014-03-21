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


class SQEkernel(base):


    tag = "SQEkernel"

    def createKernel( self, **kwds ):
        Qrange = self._parse( kwds['Q-range'] )
        Erange = self._parse( kwds['energy-range'] )

        from mccomponents.sample import sqekernel
        return sqekernel(
            Qrange = Qrange, Erange = Erange)


    def onSQE(self, sqe):
        self.element.SQE = sqe
        return

    
    onSQE_fromexpression = onGridSQE = onSQE


    pass # end of SQEkernel


# version
__id__ = "$Id$"

# End of file 
