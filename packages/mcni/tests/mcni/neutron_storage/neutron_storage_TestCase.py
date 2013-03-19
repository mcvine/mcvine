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
import mcni.neutron_storage as mns, os


import journal
debug = journal.debug( "mcni.neutron_storage.test" )
warning = journal.warning( "mcni.neutron_storage.test" )


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
        

    def test1(self):
        'neutron_storage: mix npy implementation and non-npy one'
        import mcni
        neutrons = mcni.neutron_buffer( 7 )
        out = 'tmp-nst-test1.ns'
        if os.path.exists(out): os.remove(out)
        storage = mns.storage(out, mode='w')
        storage.write(neutrons)
        neutrons1 = mns.load( 'neutrons.dat' )
        return
        

    def test2(self):
        'normalize'
        import mcni
        # create a dummy input
        neutrons = mcni.neutron_buffer( 10 )
        for n in neutrons:
            n.probability = 1
            continue
        out = 'tmp-nst-test2.ns'
        mns.dump(neutrons, out)

        # try normalize out-of-place
        out2 = 'tmp-nst-test2-normalized.ns'
        if os.path.exists(out2): os.remove(out2)
        mns.normalize(out, 10., out2)
        neutrons2 = mns.load(out2)
        # and see if it is done correctly
        for n in neutrons2:
            self.assertAlmostEqual(n.probability, .1)
            continue

        # try normalize in-place
        mns.normalize(out, 10.)
        neutrons2 = mns.load(out)
        # and see if it is done correctly
        for n in neutrons2:
            self.assertAlmostEqual(n.probability, .1)
            continue
        return
        

    def test2a(self):
        'normalize: large buffer'
        import mcni
        # create a dummy input
        neutrons = mcni.neutron_buffer( int(3e6) )
        narr = neutrons.to_npyarr()
        narr[:, -1] = 1
        neutrons.from_npyarr(narr)
        out = 'tmp-nst-test2a.ns'
        mns.dump(neutrons, out)
        del neutrons
        
        # try normalize out-of-place
        out2 = 'tmp-nst-test2a-normalized.ns'
        if os.path.exists(out2): os.remove(out2)
        mns.normalize(out, 10., out2)
        neutrons2 = mns.load(out2)
        # and see if it is done correctly
        narr = neutrons2.to_npyarr()
        self.assertTrue((narr[:, -1] == .1).all())
        del neutrons2, narr
        
        # try normalize in-place
        mns.normalize(out, 10.)
        neutrons2 = mns.load(out)
        # and see if it is done correctly
        narr = neutrons2.to_npyarr()
        self.assertTrue((narr[:, -1] == .1).all())
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
    unittest.main()
    # main()
    
# version
__id__ = "$Id$"

# End of file 
