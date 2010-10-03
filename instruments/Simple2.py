#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

__doc__ = """a simple instrument with just two components: source and monitor
"""
__author__ = 'Jiao Lin'


from mcni.pyre_support.Instrument import Instrument as base

class Instrument(base):
    
    class Inventory( base.Inventory ):

        from mcstas2.pyre_support import facility
        source = facility( 'sources', 'Source_simple', 'source' )
        monitor = facility( 'monitors', 'E_monitor', 'monitor' ) 
        pass # end of Inventory


    def __init__(self, name = 'simple2'):
        base.__init__(self, name)
        return
    

    def _defaults(self):
        base._defaults(self)
        
        self.inventory.sequence = ['source', 'monitor']
        
        geometer = self.inventory.geometer
        geometer.inventory.source = (0,0,0), (0,0,0)
        geometer.inventory.monitor = (0,0,10), (0,0,0)
        
        source = self.inventory.source
        source.inventory.dist = 10
        source.inventory.xw = 0.1
        source.inventory.yh = 0.1
        source.inventory.radius = 0.02
        source.inventory.E0 = 60
        source.inventory.dE = 5

        monitor = self.inventory.monitor
        monitor.inventory.Emin = 10
        monitor.inventory.Emax = 100
        monitor.inventory.nchan = 20
        monitor.inventory.xwidth = 0.1
        monitor.inventory.yheight = 0.1
        return
    
    pass # end of Instrument


def main():
    simple2=Instrument()
    simple2.run()
    return


if __name__ == '__main__' : main()
        

# version
__id__ = "$Id$"

#  End of file 
