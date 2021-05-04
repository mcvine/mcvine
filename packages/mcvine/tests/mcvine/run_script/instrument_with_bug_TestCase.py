#!/usr/bin/env python
#
#


import os, shutil
import mcvine.run_script

import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        outdir = 'out-instrument_with_bug-ctor'
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        with self.assertRaises(RuntimeError) as re:
            mcvine.run_script.run_mpi(
                'test_instrument_with_bug.py',
                outdir, ncount=1e5, nodes=2, overwrite_datafiles=False,
                trigger = 'process'
            )
        return

    def test2(self):
        outdir = 'out-instrument_with_bug-processing'
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        with self.assertRaises(RuntimeError) as re:
            mcvine.run_script.run_mpi(
                'test_instrument_with_bug.py',
                outdir, ncount=1e5, nodes=2, overwrite_datafiles=False,
                trigger = 'process'
            )
        return

    pass  # end of TestCase

if __name__ == "__main__": unittest.main()

# End of file
