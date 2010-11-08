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

skip = True


import unittestX as unittest
import journal

debug = journal.debug( "parallel_simulation_TestCase" )
warning = journal.warning( "parallel_simulation_TestCase" )



import mcni

class TestCase(unittest.TestCase):


    def __init__(self, *args, **kwds):
        super(TestCase, self).__init__(*args, **kwds)
        try:
            import mpi
        except ImportError:
            import warnings
            warnings.warn('no mpi. skip this test')
            self.nompi = True
        else:
            self.nompi = False
        return


    def test(self):
        if self.nompi: return
        
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
        import mpi
        rank = mpi.world().rank
        
        s = [ '%s'% n for n in neutrons ]
        print 'node %d: %s' % (rank, ', '.join(s) )
        return neutrons

    pass # end of Verifier



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    import journal
    journal.info('mpirun').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
