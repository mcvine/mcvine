#!/usr/bin/env python
#
#
import os, shutil
import mcvine.run_script

import unittest
class TestCase(unittest.TestCase):

    def test3(self):
        outdir = 'out-method-run_mpi'
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        mcvine.run_script.run_mpi('test_instrument_method.py', outdir, 1e5, nodes=2, overwrite_datafiles=False)
        mcvine.run_script.run_mpi(
            'test_instrument_method.py', outdir, 1e5, nodes=2, overwrite_datafiles=True, E0=95)
        return

    pass  # end of TestCase


if __name__ == "__main__": unittest.main()

# End of file
