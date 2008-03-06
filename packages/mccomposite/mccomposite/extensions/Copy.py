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


#sometimes ScattererCopy are just called "Copy"
from mccomposite.ScattererCopy import ScattererCopy
class Copy(ScattererCopy):
    def identify(self, visitor): return visitor.onCopy(self)
    pass # Copy

def onCopy(self, copy):
    return self.onScattererCopy(copy)


# 4. register the new class and handlers
import mccomposite
mccomposite.register_engine_renderer_handler(Copy, onCopy)


# version
__id__ = "$Id$"

# End of file 
