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


standalone = True


# from neutron_storage_normalization_TestCase-app.pml
ncount = 1e4
import os


import unittestX as unittest


class TestCase(unittest.TestCase):


    def test1(self):
        cmd = './neutron_storage_normalization_TestCase-app'
        outdir = 'out-neutron_storage_normalization_TestCase-app'
        outfile = os.path.join(outdir, 'neutrons')
        if os.system(cmd):
            raise RuntimeError, "%r failed" % cmd
        
        # make sure the final result is normalized
        from mcni.neutron_storage import readneutrons_asnpyarr
        neutrons = readneutrons_asnpyarr(outfile)
        self.assertEqual(len(neutrons), ncount)
        expected = [0., 0., -1., 
                    0., 0., 3000.,
                    0., 1.,
                    0.,
                    1.]
        for n in neutrons:
            self.assert_((n==expected).all())
            continue
        return


    def test2(self):
        cmd = './neutron_storage_normalization_TestCase-app2'
        outdir = 'out-neutron_storage_normalization_TestCase-app2'
        outfile = os.path.join(outdir, 'neutrons')
        if os.system(cmd):
            raise RuntimeError, "%r failed" % cmd
        
        # make sure the final result is normalized
        from mcni.neutron_storage import readneutrons_asnpyarr
        neutrons = readneutrons_asnpyarr(outfile)
        self.assertEqual(len(neutrons), ncount/10)
        expected = [0., 0., -1., 
                    0., 0., 3000.,
                    0., 1.,
                    0.,
                    1./10]
        for n in neutrons:
            self.assert_((n==expected).all())
            continue
        return


    pass # end of TestCase


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
