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
This test should be run from command line by calling mpiexec.
For example:

  mpiexec -n 2 `which mpipython.exe` neutron_storage_parallel_TestCase.py

Make sure 
'''

# skip = 1
standalone = 1


import unittestX as unittest
import journal

debug = journal.debug( "mcni.components.test" )
warning = journal.warning( "mcni.components.test" )


import mcni
neutron_storage_path = None
ntotneutrons = None

def _init():
    global neutron_storage_path, ntotneutrons
    try:
        import mpi
    except:
        pass
    else:
        rank = mpi.world().rank
        neutron_storage_path = 'neutrons-%d' % rank
        import os
        if os.path.exists(neutron_storage_path):
            os.remove(neutron_storage_path)
    ntotneutrons = 53

    neutron = mcni.neutron( r = (0,0,0),
                            v = (1000,2000,3000),
                            time = 0,
                            prob = 1,
                            )


from mcni.AbstractComponent import AbstractComponent
class Source( AbstractComponent ):

    def process(self, neutrons):
        for i in range(len(neutrons)):
            neutrons[i] = mcni.neutron( r = (0,0,i), v = (1000, 2000, 3000) )
            continue
        return neutrons
    
    

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



    def test0(self):
        'prepare'
        if self.nompi: return

        import os, shutil
        from mcni.utils.mpiutil import rank 
        path = neutron_storage_path
        if os.path.exists( path ): shutil.rmtree( path )
        return


    def test1(self):
        'neutron --> storage'
        if self.nompi: return

        #from mcni.components.MonochromaticSource import MonochromaticSource
        #component1 = MonochromaticSource('source', neutron)
        component1 = Source( 'source' )
        
        from mcni.components.NeutronToStorage import NeutronToStorage
        component2 = NeutronToStorage( 'storage', neutron_storage_path)
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,0), (0,0,0) )

        neutrons = mcni.neutron_buffer( ntotneutrons )

        mcni.simulate( instrument, geometer, neutrons )
        return


    pass # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    _init()
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
