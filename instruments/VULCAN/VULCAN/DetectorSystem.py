#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from mcni.pyre_components.MultiMonitors import MultiMonitors
class DetectorSystem(MultiMonitors):

    class Inventory(MultiMonitors.Inventory):
        
        from mcni.pyre_support import facility
        m1 = facility('m1', default="monitors/NDMonitor(t)")
        m2 = facility('m2', default="monitors/NDMonitor(w)")
        m3 = facility('m3', default="monitors/NDMonitor(t)")
        m4 = facility('m4', default="monitors/NDMonitor(w)")
        m5 = facility('m5', default="monitors/NDMonitor(t)")
        m6 = facility('m6', default="monitors/NDMonitor(w)")


    def _defaults(self):
        super(DetectorSystem, self)._defaults()
        geometer = self.inventory.geometer
        # geometer.inventory.m1 = (0,0,2), (0,90,0)
        return
        
        
    def _configure(self):
        super(DetectorSystem, self)._configure()
        self.monitors = [
            self.inventory.m1, 
            self.inventory.m2,
            self.inventory.m3, 
            self.inventory.m4,
            self.inventory.m5, 
            self.inventory.m6,
            ]
        return

# version
__id__ = "$Id$"

# End of file 
