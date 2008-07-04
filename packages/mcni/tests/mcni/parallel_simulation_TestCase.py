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



'''
This test needs to be run parallely using command mpiexec.

For example,

 mpiexec -n 2 `which mpipython.exe` parallel_simulation_TestCase.py

The neutrons generated in different nodes should be different.

** TODO **
Should try to automatically determine if neutrons are different.
Probably should implement that using a shell script.
'''


import unittestX as unittest
import journal

debug = journal.debug( "parallel_simulation_TestCase" )
warning = journal.warning( "parallel_simulation_TestCase" )

import mpi
rank = mpi.world().rank


import mcni

class TestCase(unittest.TestCase):


    def test(self):
        component1 = Source('source')
        component2 = Printer('printer')
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,0), (0,0,0) )

        neutrons = mcni.neutron_buffer( 2 )

        mcni.simulate( instrument, geometer, neutrons )

        return
    
        
    pass  # end of TestCase


# register random seeding function so that automatically seeds
# will be fed.
import random
from mcni.seeder import register
register( random.seed )


from mcni.AbstractComponent import AbstractComponent
class Source( AbstractComponent ):

    def process(self, neutrons):
        for i in range(len(neutrons)):
            neutrons[i] = mcni.neutron( r = ( 0,0,0 ), v = (0,0,random.random()) )
            continue
        return neutrons

    pass # end of Source


class Printer( AbstractComponent ):

    def process(self, neutrons):
        s = [ '%s'% n for n in neutrons ]
        print 'node %d: %s' % (rank, ', '.join(s) )
        return neutrons

    pass # end of Verifier


    
def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
