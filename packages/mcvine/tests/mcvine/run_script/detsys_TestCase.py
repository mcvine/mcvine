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
        outdir = 'out-detsys'
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        script = "test_instr_with_detsys.py"
        mcvine.run_script.run_mpi(
            script, workdir=outdir, ncount=int(1e5), nodes=2, buffer_size=int(1e2), overwrite_datafiles=False)
        return

    
    pass  # end of TestCase


if __name__ == "__main__": unittest.main()
    
# End of file 
