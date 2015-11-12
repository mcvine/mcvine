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


from pyre.inventory.Facility import Facility


class NeutronTracerFacility( Facility ):


    def _import(self, name):
        if name in defaults:
            locator = "<defaults>"
            return defaults[name], locator
        return super(NeutronTracerFacility, self)._import(name)


from ConsoleNeutronTracer import ConsoleNeutronTracer
defaults = {
    'console': ConsoleNeutronTracer(),
    }
            
# version
__id__ = "$Id$"

# End of file 
