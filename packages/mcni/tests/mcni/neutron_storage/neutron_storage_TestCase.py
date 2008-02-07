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
        'neutron_storage'
        from mcni.neutron_storage import load, dump
        import mcni
        neutrons = mcni.neutron_buffer( 7 )
        neutrons[5] = mcni.neutron( v = (8,9,10) )
        dump(neutrons, 'neutrons.dat')
        neutrons1 = load( 'neutrons.dat' )
        n5 = neutrons1[5]
        v = n5.state.velocity
        self.assertAlmostEqual( v[0], 8 )
        self.assertAlmostEqual( v[1], 9 )
        self.assertAlmostEqual( v[2], 10 )
        return
        
    pass  # end of TestCase



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
