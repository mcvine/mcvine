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

class Scatterer:

    def __init__(self, shape):
        self._shape = shape
        return

    def shape(self):
        return self._shape

    def identify(self, visitor):
        return visitor.onScatterer(self)

    pass # end of Scatterer
    

# version
__id__ = "$Id$"

# Generated automatically by PythonMill on Fri Dec 28 09:28:38 2007

# End of file 
