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


from .AbstractNode import AbstractNode, debug
import numpy as np


# base class for kernel nodes

class KernelNode(AbstractNode):
    
    
    def elementFactory( self, **kwds ):
        kernel = self.createKernel(**kwds)
        # weight
        weight = float(kwds.get('weight') or 1)
        if weight <= 0:
            raise ValueError("weight must be positive")
        kernel.weight = weight
        # rotmat
        rotmat = kwds.get('orientation', None)
        if rotmat is not None:
            import numpy as np
            d = dict(sqrt=np.sqrt)
            rotmat = eval(rotmat, d)
            rotmat = np.array(rotmat)
            rotmat.shape = 3,3
        kernel.rotmat = rotmat
        return kernel

    pass # end of KernelNode


# version
__id__ = "$Id$"

# End of file 
