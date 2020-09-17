#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


standalone = True
# from neutron_storage_normalization_TestCase-app.pml
ncount = 1e4


import os
os.environ['MCVINE_MPI_LAUNCHER']='serial'


import unittestX as unittest


class TestCase(unittest.TestCase):


    def test1(self):
        cmd = './neutron_storage_normalization_TestCase-app'
        outdir = 'out-neutron_storage_normalization_TestCase-app'
        outfile = os.path.join(outdir, 'neutrons')
        if os.system(cmd):
            raise RuntimeError("%r failed" % cmd)
        
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
            self.assertTrue((n==expected).all())
            continue
        return


    def test2(self):
        cmd = './neutron_storage_normalization_TestCase-app2'
        outdir = 'out-neutron_storage_normalization_TestCase-app2'
        outfile = os.path.join(outdir, 'neutrons')
        if os.system(cmd):
            raise RuntimeError("%r failed" % cmd)
        
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
            self.assertTrue((n==expected).all())
            continue
        return


    pass # end of TestCase


if __name__ == "__main__":  unittest.main()
    
# End of file 
