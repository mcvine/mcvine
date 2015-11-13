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


class ScattererCopy:
    
    'copy of a scatterer'
    
    def __init__(self, reference, id = 0):
        self._reference = reference
        self._id = id
        return

    def reference(self): return self._reference

    def id(self): return self._id
    
    def identify(self, visitor): return visitor.onScattererCopy(self)
    
    pass


# version
__id__ = "$Id$"

# Generated automatically by PythonMill on Fri Dec 28 09:28:38 2007

# End of file 
