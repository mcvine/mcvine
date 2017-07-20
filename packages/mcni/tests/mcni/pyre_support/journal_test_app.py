#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


import os
os.environ['MCVINE_MPI_LAUNCHER'] = 'serial'


from mcni.pyre_support.MpiApplication import Application as base
class App(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        pass # end of Inventory


    def main(self):
        super(App, self).main()
        self._debug.log("hello")
        return


if __name__ == "__main__": App('journal_test_app').run()
    
# End of file 
