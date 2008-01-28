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

class Info:

    def __init__(self, root = None, include = None, lib = None, bin = None, **kwds):
        self.root = root
        self.include = include
        self.lib = lib
        self.bin = bin
        self.__dict__.update( kwds )
        return

    pass # end of Info


# version
__id__ = "$Id$"

# End of file 
