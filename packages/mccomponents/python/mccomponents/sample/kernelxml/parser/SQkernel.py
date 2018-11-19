#!/usr/bin/env python
#
#


from .KernelNode import KernelNode as base, debug


class SQkernel(base):


    tag = "SQkernel"

    def createKernel( self, **kwds ):
        Qrange = self._parse( kwds['Q-range'] )

        from mccomponents.sample import sqkernel
        return sqkernel(Qrange = Qrange)


    def onSQ(self, sq):
        self.element.SQ = sq
        return

    
    onSQ_fromexpression = onGridSQ = onSQ


    pass # end of SQkernel


# End of file 
