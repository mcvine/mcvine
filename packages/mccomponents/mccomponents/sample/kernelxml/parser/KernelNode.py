#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C) 2007-2014   All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractNode import AbstractNode, debug


# base class for kernel nodes

class KernelNode(AbstractNode):
    
    
    def elementFactory( self, **kwds ):
        weight = float(kwds.get('weight') or 1)
        if weight <= 0:
            raise ValueError("weight must be positive")
        kernel = self.createKernel(**kwds)
        kernel.weight = weight
        return kernel

    pass # end of KernelNode


# version
__id__ = "$Id$"

# End of file 
