#!/usr/bin/env python
#
#


import os, shutil
import mcvine.run_script
import histogram.hdf as hh, numpy as np

os.environ['MCVINE_DEBUG_PARALLEL_PPS'] = 'yes'

import unittest
class TestCase(unittest.TestCase):


    def test1(self):
        outdir = 'out-instrument-run1'
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        mcvine.run_script.run1('test_instrument.py', outdir, 1e5, overwrite_datafiles=False)
        mcvine.run_script.run1('test_instrument.py', outdir, 1e5, overwrite_datafiles=True)
        with self.assertRaises(IOError):
            mcvine.run_script.run1('test_instrument.py', outdir, 1e5, overwrite_datafiles=False)
        return

    def test2(self):
        outdir = 'out-instrument-run1_mpi'
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        mcvine.run_script.run1_mpi('test_instrument.py', outdir, 1e5, overwrite_datafiles=False)
        mcvine.run_script.run1_mpi('test_instrument.py', outdir, 1e5, overwrite_datafiles=True)
        with self.assertRaises(IOError):
            mcvine.run_script.run1_mpi('test_instrument.py', outdir, 1e5, overwrite_datafiles=False)
        return

    pass  # end of TestCase



if __name__ == "__main__":
    import journal
    journal.info("instrument").activate()
    unittest.main()

# End of file
