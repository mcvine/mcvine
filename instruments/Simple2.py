#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#              (C) 2005 All Rights Reserved  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

__doc__ = """a simple instrument with just two components: source and monitor
"""
__author__ = 'Jiao Lin'


from simulation.simulation.Instrument import Instrument as Base
from simulation.neutron_comp.pyre.source import TrivSource
from simulation.neutron_comp.pyre import NeutronPrinter


class Simple2(Base):

    '''
    A trivial 2-components instrument.

    component #1: source
    component #2: detector
    '''

    class Inventory(Base.Inventory):
        
        import pyre
        
        source = pyre.inventory.facility('source', factory = TrivSource, args = ["monochromatic"] )
        
        detector = pyre.inventory.facility('detector', factory = NeutronPrinter, args = ['printer'])


    def __init__(self, name = "Simple2"):
        Base.__init__(self, name)
        return 


    def neutron_comp_list(self):
        return ['source', 'detector']


    def _defaults(self):
        Base._defaults(self)
        self.inventory.ncount = 10
        self.inventory.buffer_size = 10
        self.inventory.dir = "__simple2_results__"
        self.inventory.overwrite_datafiles = True
        return


def main():
    simple2=Simple2()
    simple2.run()
    return


if __name__ == '__main__' : main()
        

# version
__id__ = "$Id: Simple2.py 578 2006-08-06 19:42:55Z linjiao $"

#  End of file 
