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

__doc__ = '''
To run this test case, you will need to use the following command line::

 $ mpirun -np 3 `which mpipython.exe` neutron_storage_mpi_TestCase.py
 
'''

skip = 1


import unittestX as unittest



neutron_storage_path = 'neutrons-saved'
ntotneutrons = 3

import mcni
mpirank = None

def _init():
    neutrons = mcni.neutron_buffer(ntotneutrons)
    for i in range(ntotneutrons):
        neutrons[i] = mcni.neutron(
            r = (0,0,i),
            )
        continue

    from mcni.utils import mpi
    global mpirank
    mpirank = mpi.rank
    mpisize = mpi.world.size
    if mpisize != 3:
        raise RuntimeError(__doc__)

    import os
    channel = 1000
    if mpirank == 0:
        if os.path.exists(neutron_storage_path):
            os.remove(neutron_storage_path)
        from mcni.neutron_storage.Storage import Storage
        storage = Storage(neutron_storage_path, 'w')
        storage.write(neutrons)
        del storage
        for i in range(1, mpisize):
            mpi.send(0, i, channel)
            continue
    else:
        mpi.receive(0, channel)


from mcni.AbstractComponent import AbstractComponent
class Verifier( AbstractComponent ):

    def __init__(self, name, testFacility):
        AbstractComponent.__init__(self, name)
        self.testFacility = testFacility
        return

    def process(self, neutrons):
        tf = self.testFacility
        tf.assertEqual(len(neutrons), 1)
        tf.assertEqual(neutrons[0].state.position[2], mpirank)
        return neutrons

    pass # end of Verifier



class TestCase(unittest.TestCase):


    def test1(self):
        
        from mcni.components.NeutronFromStorage import NeutronFromStorage
        component1 = NeutronFromStorage('storage', neutron_storage_path)
        component2 = Verifier( 'verifier', self)
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,0), (0,0,0) )
        
        neutrons = mcni.neutron_buffer( 1 )

        mcni.simulate( instrument, geometer, neutrons )
        return

    pass # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    _init()
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
