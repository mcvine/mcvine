#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


import random
import logging
# Configure the basic logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MCVine")

from mcni.pyre_support.AbstractComponent import AbstractComponent

class Source( AbstractComponent ):

    def process(self, neutrons):
        import mcni
        for i in range(len(neutrons)):
            logger.info("loop #%d" % i)
            neutrons[i] = mcni.neutron( r = ( 0,0,0 ), v = (0,0,random.random()) )
            continue
        return neutrons

    pass # end of Source


from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        from mcni.pyre_support import facility
        source = facility('source', default = Source('source') )

        pass # end of Inventory

    def _defaults(self):
        base._defaults(self)
        self.inventory.sequence = ['source']
        return

    pass # end of Instrument


if __name__ == "__main__": Instrument("journal_test_sim_app").run()

# End of file 