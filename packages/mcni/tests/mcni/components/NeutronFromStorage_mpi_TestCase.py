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


"""
To run this test

1. make sure mpd are started
 e.g. mpdboot -f ~/mpd.hosts
2. run
 mpirun -n 5 `which mpipython.exe` NeutronFromStorage_mpi_TestCase.py
"""


skip = 1
needmpi = 1

import unittestX as unittest



class TestCase(unittest.TestCase):


    def test1(self):
        'NeutronFromStorage'
        from mcni.components.NeutronFromStorage import NeutronFromStorage
        comp = NeutronFromStorage('storage', 'neutron-storage-for-NeutronFromStorage_TestCase')

        from mcni.utils import mpi
        mpisize = mpi.world.size
        mpirank = mpi.rank
        
        from mcni import neutron_buffer
        neutrons = neutron_buffer(1)
        comp.process(neutrons)
        self.assertEqual(neutrons[0].probability, mpirank*10+9)
        comp.process(neutrons)
        self.assertEqual(neutrons[0].probability, mpisize*10+mpirank*10+9)
        return


    pass # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    return


if __name__ == "__main__":  main()

    
# version
__id__ = "$Id$"

# End of file 
