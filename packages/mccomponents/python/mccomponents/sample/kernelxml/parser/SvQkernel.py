#!/usr/bin/env python
#
#


from .KernelNode import KernelNode as base, debug


class SvQkernel(base):

    tag = "SvQkernel"

    def createKernel( self, **kwds ):
        from mccomponents.sample import svqkernel
        return svqkernel()

    def onSvQ(self, svq):
        self.element.SvQ = svq
        return

    # onSvQ_fromexpression =
    onGridSvQ = onSvQ

    pass # end of SvQkernel


# End of file
