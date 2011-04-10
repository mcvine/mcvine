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
            os.remove( path )
        
        from mcni.neutron_storage.Storage import Storage

        #open storage for writing
        s = Storage( path, 'w' )

        #create neutrons
        import mcni
        neutrons = mcni.neutron_buffer( 7 )
        neutrons[5] = mcni.neutron( v = (8,9,10) )

        #write neutrons
        s.write( neutrons )

        #delete the storage to make sure it flushes all neutrons
        del s

        #open the storage for reading
        sr = Storage( path, 'r')
        neutrons = sr.read()
        self.assertEqual( len(neutrons), 7 )

        self.assertAlmostEqual( neutrons[5].state.velocity[0] , 8 )
        return
    
        
    def test2(self):
        'neutron_storage.Storage: write 2 packets'

        path = 'test-storage-2'
        if os.path.exists(path):
            os.remove( path )
        
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

        # flush
        del s
        
        #open the storage for reading
        sr = Storage( path, 'r', packetsize=7)

        neutrons = sr.read()
        self.assertEqual( len(neutrons), 7 )
        self.assertAlmostEqual( neutrons[5].state.velocity[0] , 8 )
        
        neutrons = sr.read()
        self.assertEqual( len(neutrons), 7 )
        self.assertAlmostEqual( neutrons[5].state.velocity[0] , 8 )
        return
        

    def test3(self):
        'neutron_storage.Storage: wrap-reading (nread>ntotal)'

        path = 'test-storage-3'
        if os.path.exists(path):
            os.remove( path )
        
        from mcni.neutron_storage.Storage import Storage

        #open storage for writing
        s = Storage( path, 'w' )

        #create neutrons
        import mcni
        neutrons = mcni.neutron_buffer( 7 )
        for i in range(7):
            neutrons[i] = mcni.neutron( v = (i,0,0) )

        #write 
        s.write( neutrons )

        # flush
        del s
        
        #open the storage for reading
        sr = Storage( path, 'r', packetsize=10)

        neutrons = sr.read()
        self.assertEqual( len(neutrons), 10 )
        self.assertAlmostEqual( neutrons[5].state.velocity[0] , 5 )
        self.assertAlmostEqual( neutrons[9].state.velocity[0] , 2 )

        neutrons = sr.read()
        self.assertAlmostEqual( neutrons[0].state.velocity[0] , 3 )
        return

        
    def test4(self):
        'neutron_storage.Storage: wrap-reading (nread<ntotal)'

        path = 'test-storage-4'
        if os.path.exists(path):
            os.remove( path )
        
        from mcni.neutron_storage.Storage import Storage

        #open storage for writing
        s = Storage( path, 'w' )

        #create neutrons
        import mcni
        neutrons = mcni.neutron_buffer( 7 )
        for i in range(7):
            neutrons[i] = mcni.neutron( v = (i,0,0) )

        #write 
        s.write( neutrons )

        # flush
        del s
        
        #open the storage for reading
        sr = Storage( path, 'r', packetsize=5)

        neutrons = sr.read()
        self.assertEqual( len(neutrons), 5 )
        self.assertAlmostEqual( neutrons[3].state.velocity[0] , 3 )
        self.assertAlmostEqual( neutrons[4].state.velocity[0] , 4 )

        neutrons = sr.read()
        self.assertEqual( len(neutrons), 5 )
        self.assertAlmostEqual( neutrons[0].state.velocity[0] , 5 )
        self.assertAlmostEqual( neutrons[4].state.velocity[0] , 2 )

        return

        
    def test5(self):
        'neutron_storage.Storage: wrap-reading (nread>>ntotal)'

        path = 'test-storage-4'
        if os.path.exists(path):
            os.remove( path )
        
        from mcni.neutron_storage.Storage import Storage

        #open storage for writing
        s = Storage( path, 'w' )

        #create neutrons
        import mcni
        neutrons = mcni.neutron_buffer( 5 )
        for i in range(5):
            neutrons[i] = mcni.neutron( v = (i,0,0) )

        #write 
        s.write( neutrons )

        # flush
        del s
        
        #open the storage for reading
        sr = Storage( path, 'r')

        neutrons = sr.read(100)
        self.assertEqual( len(neutrons), 100 )
        self.assertAlmostEqual( neutrons[3].state.velocity[0] , 3 )
        self.assertAlmostEqual( neutrons[4].state.velocity[0] , 4 )
        self.assertAlmostEqual( neutrons[6].state.velocity[0] , 1 )
        self.assertAlmostEqual( neutrons[7].state.velocity[0] , 2 )

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
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
