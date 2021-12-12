#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, shutil, numpy as np, histogram.hdf as hh
import mcvine.resources as mr
import unittest
import psutil
nodes = max(psutil.cpu_count()//2, 1)

class SNS_source_TestCase(unittest.TestCase):

    def test(self):
        fn = './BL20-CY-123D-STS-Min-2G-source_mctal-195_sp.dat'
        import mcvine.run_script
        mcvine.run_script.run_mpi(
            './myinstrument.py', "out", 1e7,
            nodes=nodes,
            overwrite_datafiles=True,
            moderator_datafile = fn,
        )
        # I(tof)
        expected = hh.load('./expected/I_tof.h5')
        result = hh.load('./out/I_tof.h5')
        print(result.I)
        rdiff = np.abs(result.I[17:-15] - expected.I[17:-15])/expected.I[17:-15]
        print((rdiff<0.08).sum(), rdiff.size)
        self.assert_((rdiff<0.08).sum() >= rdiff.size*.9)
        # I(lambda)
        expected = hh.load('./expected/I_lambda.h5')
        result = hh.load('./out/I_lambda.h5')
        rdiff = np.abs(result.I[5:-5] - expected.I[5:-5])/expected.I[5:-5]
        print(result.I)
        print((rdiff<0.05).sum(), rdiff.size)
        self.assert_((rdiff<0.05).sum() >= rdiff.size*.85)
        return

    pass

if __name__ == "__main__": unittest.main()

# End of file
