#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2010 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import mcvine

from mcni.pyre_components.MultiMonitors import MultiMonitors
class MyMonitor(MultiMonitors):

    class Inventory(MultiMonitors.Inventory):
        
        from mcni.pyre_support import facility
        m1 = facility('m1', default="mcni://monitors/NeutronPrinter")
        m2 = facility('m2', default="mcni://monitors/NeutronPrinter")

    def _configure(self):
        super(MyMonitor, self)._configure()
        self.monitors = [self.inventory.m1, self.inventory.m2]
        return


from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        from mcni.pyre_support import facility
        
        source = facility('source', default='mcni://sources/MonochromaticSource')
        monitor = facility('monitor', default=MyMonitor('monitor'))

    def _defaults(self):
        super(Instrument, self)._defaults()
        self.inventory.sequence = ['source', 'monitor']
        self.inventory.ncount = 2
        self.inventory.buffer_size = 2
        self.inventory.overwrite_datafiles = 1
        return

    pass # end of Instrument


def main():
    app = Instrument('testapp1')
    app.run()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
