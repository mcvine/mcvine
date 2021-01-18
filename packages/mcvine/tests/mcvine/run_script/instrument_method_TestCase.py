#!/usr/bin/env python
#
#


import os, shutil
import mcvine.run_script

import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        outdir = 'out-method-run1'
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        mcvine.run_script.run1('test_instrument_method.py', outdir, 1e5, overwrite_datafiles=False)
        mcvine.run_script.run1('test_instrument_method.py', outdir, 1e5, overwrite_datafiles=True, E0=95)
        return

    def test2(self):
        outdir = 'out-method-run1_mpi'
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        mcvine.run_script.run1_mpi('test_instrument_method.py', outdir, 1e5, overwrite_datafiles=False)
        mcvine.run_script.run1_mpi('test_instrument_method.py', outdir, 1e5, overwrite_datafiles=True, E0=95)
        return

    pass  # end of TestCase



if __name__ == "__main__": unittest.main()

# End of file
