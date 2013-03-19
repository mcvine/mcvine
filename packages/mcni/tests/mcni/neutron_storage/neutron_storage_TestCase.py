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

import mcni.neutron_storage as mns


class TestCase(unittest.TestCase):


    def test(self):
        'neutron_storage'
        import mcni
        neutrons = mcni.neutron_buffer( 7 )
        neutrons[5] = mcni.neutron( v = (8,9,10) )
        mns.dump(neutrons, 'neutrons.dat')
        neutrons1 = mns.load( 'neutrons.dat' )
        n5 = neutrons1[5]
        v = n5.state.velocity
        self.assertAlmostEqual( v[0], 8 )
        self.assertAlmostEqual( v[1], 9 )
        self.assertAlmostEqual( v[2], 10 )
        return
        

    def test2(self):
        'normalize'
        import mcni
        neutrons = mcni.neutron_buffer( 10 )
        for n in neutrons:
            n.probability = 1
            continue
        out = 'tmp-nst-test2.ns'
        mns.dump(neutrons, out)
        mns.normalize(out, 10.)
        neutrons2 = mns.load(out)
        for n in neutrons2:
            self.assertAlmostEqual(n.probability, .1)
            continue
        return
        
    pass  # end of TestCase



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
