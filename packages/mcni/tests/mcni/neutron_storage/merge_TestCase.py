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
        'neutron_storage.merge'

        oldstorage_path = 'test-merge-old'
        newstorage_path = 'test-merge-new'
        newpacketsize = 10

        for path in [ oldstorage_path, newstorage_path ]:
            if os.path.exists( path ):
                os.remove( path )
            continue
        
        from mcni.neutron_storage import storage, merge

        #open storage for writing
        s = storage( oldstorage_path, 'w' )

        #create neutrons
        import mcni
        neutrons = mcni.neutron_buffer( 7 )
        neutrons[5] = mcni.neutron( v = (8,9,10) )

        #write neutrons
        s.write( neutrons )
        s.write( neutrons )
        s.write( neutrons )
        #important!!! flush the storage
        del s

        #merge
        merge([oldstorage_path], newstorage_path)

        #open the merged storage for reading
        sr = storage( newstorage_path, 'r')
        neutrons = sr.read()
        self.assertEqual( len(neutrons), 7*3 )

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
