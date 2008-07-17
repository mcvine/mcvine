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

debug = journal.debug( "mcni.neutron_storage.test" )
warning = journal.warning( "mcni.neutron_storage.test" )



class TestCase(unittest.TestCase):


    def test(self):
        'neutron_storage.Storage: write and then read'

        path = 'test-storage'
        if os.path.exists(path):
            import shutil
            shutil.rmtree( path )
        
        from mcni.neutron_storage.Storage import Storage

        #open storage for writing
        s = Storage( path, 'w' )

        #create neutrons
        import mcni
        neutrons = mcni.neutron_buffer( 7 )
        neutrons[5] = mcni.neutron( v = (8,9,10) )

        #write neutrons
        s.write( neutrons )

        #open the storage for reading
        sr = Storage( path, 'r')
        self.assertEqual( sr.npackets(), 1 )
        neutrons = sr.read(0)
        self.assertEqual( len(neutrons), 7 )

        self.assertAlmostEqual( neutrons[5].state.velocity[0] , 8 )
        return
    
        
    def test2(self):
        'neutron_storage.Storage: write 2 packets'

        path = 'test-storage-2'
        if os.path.exists(path):
            import shutil
            shutil.rmtree( path )
        
        from mcni.neutron_storage.Storage import Storage

        #open storage for writing
        s = Storage( path, 'w' )

        #create neutrons
        import mcni
        neutrons = mcni.neutron_buffer( 7 )
        neutrons[5] = mcni.neutron( v = (8,9,10) )

        #write packet 1
        s.write( neutrons )

        #write packet 2
        s.write( neutrons )
        
        #open the storage for reading
        sr = Storage( path, 'r')
        self.assertEqual( sr.npackets(), 2 )

        neutrons = sr.read(0)
        self.assertEqual( len(neutrons), 7 )
        self.assertAlmostEqual( neutrons[5].state.velocity[0] , 8 )
        
        neutrons = sr.read(1)
        self.assertEqual( len(neutrons), 7 )
        self.assertAlmostEqual( neutrons[5].state.velocity[0] , 8 )
        return
        
    pass  # end of TestCase


import os



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
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
