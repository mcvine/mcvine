#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, shutil, numpy as np, histogram.hdf as hh
import mcvine.resources as mr
import unittest

class SNS_source_TestCase(unittest.TestCase):

    def test(self):
        fn = 'source_sct521_bu_17_1.dat'
        mod_data = os.path.join(mr.instrument('ARCS'), 'moderator', fn)
        shutil.copyfile(mod_data, fn)
        import mcvine.run_script
        mcvine.run_script.run_mpi(
            './myinstrument.py', "out", 3e6,
            nodes=1,
            overwrite_datafiles=True,
        )
        # I(tof)
        expected = hh.load('./expected/I_tof.h5')
        result = hh.load('./out/I_tof.h5')
        rdiff = np.abs(result.I[20:-5] - expected.I[20:-5])/expected.I[20:-5]
        self.assert_((rdiff<0.05).sum() > rdiff.size*.65)
        # I(lambda)
        expected = hh.load('./expected/I_lambda.h5')
        result = hh.load('./out/I_lambda.h5')
        rdiff = np.abs(result.I[20:-5] - expected.I[20:-5])/expected.I[20:-5]
        self.assert_((rdiff<0.05).sum() > rdiff.size*.80)
        return

    pass

if __name__ == "__main__": unittest.main()

# End of file
