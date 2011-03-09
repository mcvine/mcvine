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

        import pyre.inventory as inv
        xwidth  = inv.float( name = 'xwidth', default = 0.77)
        yheight = inv.float( name = 'yheight', default = 0.385)
        tmin    = inv.float( name = 'tmin', default = 0.)
        tmax    = inv.float( name = 'tmax', default = 0.1)
        nt      = inv.int( name = 'nt', default = 100)
        wmin    = inv.float( name = 'wmin', default = 0.)
        wmax    = inv.float( name = 'wmax', default = 10)
        nw      = inv.int( name = 'nw', default = 100)
        

    def _defaults(self):
        super(DetectorSystem, self)._defaults()
        geometer = self.inventory.geometer
        # geometer.inventory.m1 = (0,0,2), (0,90,0)
        return
        
        
    def _configure(self):
        super(DetectorSystem, self)._configure()
        self.monitors = [
            self.inventory.m1,  # middle, time
            self.inventory.m2,  # middle, wavelength
            self.inventory.m3,  # top, time
            self.inventory.m4,  # top, wavelength
            self.inventory.m5,  # bottom, time
            self.inventory.m6,  # bottom, wavelength
            ]

        geometer = self.inventory.geometer
        
        # XXX: make it shorter :)
        m1 = self.inventory.m1
        m1.inventory.xwidth  = self.inventory.xwidth
        m1.inventory.yheight = self.inventory.yheight
        m1.inventory.tmin    = self.inventory.tmin
        m1.inventory.tmax    = self.inventory.tmax
        m1.inventory.nt      = self.inventory.nt
        m1.inventory.title   = "m1"
        m1.inventory.filename = "m1.h5"
        geometer.inventory.m1 = "((-2, 0, 0), (0, 90, 0))"

        m2 = self.inventory.m2
        m2.inventory.xwidth  = self.inventory.xwidth
        m2.inventory.yheight = self.inventory.yheight
        m2.inventory.wmin    = self.inventory.tmin
        m2.inventory.wmax    = self.inventory.tmax
        m2.inventory.nw      = self.inventory.nt
        m2.inventory.title   = "m2"
        m2.inventory.filename = "m2.h5"
        geometer.inventory.m2 = "((-2, 0, 0), (0, 90, 0))"

        m3 = self.inventory.m3
        m3.inventory.xwidth  = self.inventory.xwidth
        m3.inventory.yheight = self.inventory.yheight
        m3.inventory.tmin    = self.inventory.tmin
        m3.inventory.tmax    = self.inventory.tmax
        m3.inventory.nt      = self.inventory.nt
        m3.inventory.title   = "m3"
        m3.inventory.filename = "m3.h5"
        geometer.inventory.m3 = "((-1.959, 0.403, 0), (0, 90, 0))"

        m4 = self.inventory.m4
        m4.inventory.xwidth  = self.inventory.xwidth
        m4.inventory.yheight = self.inventory.yheight
        m4.inventory.wmin    = self.inventory.tmin
        m4.inventory.wmax    = self.inventory.tmax
        m4.inventory.nw      = self.inventory.nt
        m4.inventory.title   = "m4"
        m4.inventory.filename = "m4.h5"
        geometer.inventory.m4 = "((-1.959, 0.403, 0), (0, 90, 0))"

        m5 = self.inventory.m5
        m5.inventory.xwidth  = self.inventory.xwidth
        m5.inventory.yheight = self.inventory.yheight
        m5.inventory.tmin    = self.inventory.tmin
        m5.inventory.tmax    = self.inventory.tmax
        m5.inventory.nt      = self.inventory.nt
        m5.inventory.title   = "m5"
        m5.inventory.filename = "m5.h5"
        geometer.inventory.m5 = "((-1.959, -0.403, 0), (0, 90, 0))"

        m6 = self.inventory.m6
        m6.inventory.xwidth  = self.inventory.xwidth
        m6.inventory.yheight = self.inventory.yheight
        m6.inventory.wmin    = self.inventory.tmin
        m6.inventory.wmax    = self.inventory.tmax
        m6.inventory.nw      = self.inventory.nt
        m6.inventory.title   = "m6"
        m6.inventory.filename = "m6.h5"
        geometer.inventory.m6 = "((-1.959, -0.403, 0), (0, 90, 0))"

        return

# version
__id__ = "$Id$"

# End of file 
