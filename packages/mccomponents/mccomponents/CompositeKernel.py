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



class CompositeKernel:
    

    def __init__(self):
        self._elements = []
        return


    def addElement(self, kernel):
        self._elements.append(kernel)
        return


    def elements(self): return self._elements


    def identify(self, visitor): return visitor.onCompositeKernel(self)


    pass # end of CompositeKernel



# version
__id__ = "$Id$"


# End of file 
