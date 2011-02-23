#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# this component is a powerful component that works for any vitess
# module. The purpose is to allow users to use any vitess module
# he is familiar with.

from ..Component import Component


category = "optics"


class Vitess(Component):

    def __init__(self, name, modulename=None, **kwds):
        super(Vitess, self).__init__(name, modulename, kwds)
        return

    
    pass # end of NDMonitor


# version
__id__ = "$Id$"

# End of file 
