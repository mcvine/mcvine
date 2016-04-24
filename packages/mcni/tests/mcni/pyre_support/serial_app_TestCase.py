#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


standalone = True

import os
os.environ['MCVINE_MPI_LAUNCHER'] = 'serial'


import unittestX as unittest
import journal

debug = journal.debug( "mcni.pyre_support.test" )
warning = journal.warning( "mcni.pyre_support.test" )


class TestCase(unittest.TestCase):


    def test(self):
        'mcni.pyre_support: serial_app'
        instrument = App('test-serial-app')
        instrument.testFacility = self
        instrument.run()
        return
    
        
    pass  # end of TestCase



from mcni.pyre_support.MpiApplication import Application as base
class App(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        pass # end of Inventory


    def main(self):
        super(App, self).main()
        print "in app.main()"
        return



if __name__ == "__main__": unittest.main()
    
# End of file 
