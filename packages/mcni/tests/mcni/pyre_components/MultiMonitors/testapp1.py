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


import os
os.environ['MCVINE_MPI_LAUNCHER'] = 'serial'

import mcvine


from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        from mcni.pyre_support import facility
        
        source = facility('source', default='mcni://sources/MonochromaticSource')
        monitor = facility('monitor', default='twomonitors')

    def _defaults(self):
        super(Instrument, self)._defaults()
        self.inventory.sequence = ['source', 'monitor']
        self.inventory.ncount = 2
        self.inventory.overwrite_datafiles = 1
        return

    pass # end of Instrument


def main():
    app = Instrument('testapp1')
    app.run()
    app.run_postprocessing()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
