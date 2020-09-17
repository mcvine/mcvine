#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


standalone = True

ncount = 10
n_multiple_scattering = 1

import os
os.environ['MCVINE_MPI_LAUNCHER'] = 'serial'


import mcvine


import unittestX as unittest

class TestCase(unittest.TestCase):


    def test(self):
        'mcni.pyre_support: multiple scattering'
        instrument = Instrument('multiple_scattering_Instrument_TestCase')
        instrument.testFacility = self
        instrument.run()

        self.assertEqual(instrument.inventory.counter.ntot, ncount+n_multiple_scattering)
        return
    
        
    pass  # end of TestCase



from mcni.pyre_support.AbstractComponent import AbstractComponent

class Source( AbstractComponent ):
    
    def process(self, neutrons):
        raise RuntimeError("this method should not be called")


    def processM(self, neutrons):
        # append neutrons[0] to array "neutrons"
        neutrons.append(neutrons, 0, n_multiple_scattering)
        return neutrons

    pass # end of Source


class Counter(AbstractComponent):

    def _init(self):
        super(Counter, self)._init()
        self.ntot = 0
        return
    
    
    def processM(self, neutrons):
        self.ntot += len(neutrons)
        return neutrons


from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        from mcni.pyre_support import facility
        source = facility('source', default = Source('source') )
        counter = facility('counter', default = Counter('counter') )

        pass # end of Inventory


    def _defaults(self):
        base._defaults(self)
        self.inventory.mode = 'worker'
        from mcni.pyre_support.LauncherSerial import LauncherSerial
        self.inventory.launcher = LauncherSerial()
        self.inventory.sequence = ['source', 'counter']
        geometer = self.inventory.geometer
        self.inventory.geometer.inventory.source = (0,0,0), (0,0,0)
        
        self.inventory.multiple_scattering = 1
        self.inventory.buffer_size = ncount
        self.inventory.ncount = ncount
        
        self.inventory.overwrite_datafiles = True
        return
    
    
    pass # end of Instrument


def main():
    unittest.main()
    return


if __name__ == "__main__":
    main()

    
# version
__id__ = "$Id$"

# End of file 
