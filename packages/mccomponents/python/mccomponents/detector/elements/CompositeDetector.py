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


from mccomposite.CompositeScatterer import CompositeScatterer as base

class CompositeDetector(base):
    
    def __init__(self, shape, id = 0):
        base.__init__(self, shape)
        self._id = id
        return
    
    def id(self): return self._id
    
    def identify(self, visitor): return visitor.onCompositeDetector(self)
    
    pass


# version
__id__ = "$Id$"

# End of file 
