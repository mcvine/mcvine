#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


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
        from mcni.utils.mpi import rank as mpirank, send, receive, world
        
        tag = 999
        if mpirank != 0:
            arr = n2a( self.inventory.recorder.neutrons )
            print("Node %s: sending array of shape %s" % (mpirank, arr.shape,))
            send(arr , 0, tag )
        else:
            for peer in range(1, world.size):
                arr = receive( peer, tag )
                arr.shape = -1, ndblsperneutron
                neutrons[ peer ] = a2n( arr )
                print("Node %s: received array of shape %s" % (mpirank, arr.shape))
                continue
            neutrons[ 0] = self.inventory.recorder.neutrons

        #compare
        if mpirank == 0:
            for peer in range(1, world.size):
                assert neutrons[0][0].state.velocity[2] != neutrons[peer][0].state.velocity[2]
                continue
        return


    def _defaults(self):
        base._defaults(self)
        self.inventory.sequence = ['source', 'recorder']
        geometer = self.inventory.geometer
        self.inventory.geometer.inventory.recorder = (0,0,0), (0,0,0)
        return
    
    pass # end of Instrument


if __name__ == "__main__": Instrument("parallel_simulation_TestCase").run()
    
# End of file 
