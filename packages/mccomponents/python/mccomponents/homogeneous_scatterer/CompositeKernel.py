#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from .Kernel import Kernel
class CompositeKernel(Kernel):
    

    def __init__(self, average=None, weight=None):
        self._elements = []
        self.average = average
        # weight is already handled by mccomponents.sample.kernelxml.parser.KernelNode
        return


    def addElement(self, kernel):
        self._elements.append(kernel)
        return


    def elements(self): return self._elements


    def identify(self, visitor): return visitor.onCompositeKernel(self)


    def setScattererOrigin(self, origin):
        for e in self._elements:
            e.setScattererOrigin(origin)
            continue
        return


    pass # end of CompositeKernel



# version
__id__ = "$Id$"


# End of file 
