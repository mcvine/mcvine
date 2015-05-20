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



import unittestX as unittest
import journal

debug = journal.debug( "mcni.pyre_support.test" )
warning = journal.warning( "mcni.pyre_support.test" )



class TestCase(unittest.TestCase):


    def test(self):
        'mcni.pyre_support: parallel simulation'
        instrument = Instrument('parallel_simulation_TestCase')
        instrument.testFacility = self
        instrument.run()
        return
    
        
    pass  # end of TestCase



import random
from mcni.seeder import register
register(random.seed)
del register

from mcni.pyre_support.AbstractComponent import AbstractComponent

class Source( AbstractComponent ):

    def process(self, neutrons):
        import mcni
        for i in range(len(neutrons)):
            neutrons[i] = mcni.neutron( r = ( 0,0,0 ), v = (0,0,random.random()) )
            continue
        return neutrons

    pass # end of Source


class Recorder( AbstractComponent ):

    def process(self, neutrons):
        self.neutrons = neutrons
        return neutrons

    pass # end of Recorder


from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        from mcni.pyre_support import facility
        source = facility('source', default = Source('source') )
        recorder = facility('recorder', default = Recorder( 'recorder' ) )

        pass # end of Inventory


    def main(self):
        base.main(self)

        neutrons = {}
        
        #get neutrons from other nodes
        from mcni.neutron_storage import neutrons_from_npyarr as a2n, neutrons_as_npyarr as n2a, ndblsperneutron
        from mcni.utils.mpiutil import rank as mpirank, send, receive, world
        
        tag = 999
        if mpirank != 0:
            arr = n2a( self.inventory.recorder.neutrons )
            send(arr , 0, tag )
        else:
            for peer in range(1, world.size):
                arr = receive( peer, tag )
                arr.shape = -1, ndblsperneutron
                neutrons[ peer ] = a2n( arr )
                continue
            neutrons[ 0] = self.inventory.recorder.neutrons

        #compare
        testFacility = self.testFacility
        if mpirank == 0:
            for peer in range(1, world.size):
                testFacility.assertNotEqual(
                    neutrons[0][0].state.velocity[2],
                    neutrons[peer][0].state.velocity[2],
                    )
                continue
        return


    def _defaults(self):
        base._defaults(self)
        self.inventory.sequence = ['source', 'recorder']
        geometer = self.inventory.geometer
        self.inventory.geometer.inventory.recorder = (0,0,0), (0,0,0)
        return
    
    pass # end of Instrument


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    import journal
    journal.info('mpirun').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
