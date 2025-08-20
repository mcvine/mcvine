#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


import os
os.environ['MCVINE_MPI_LAUNCHER'] = 'serial'

import logging
# Configure the basic logging setup
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MCVine")


from mcni.pyre_support.MpiApplication import Application as base
class App(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        pass # end of Inventory


    def main(self):
        super(App, self).main()
        logger.debug("hello")
        return


if __name__ == "__main__": App('logging_test_app').run()

# End of file 
