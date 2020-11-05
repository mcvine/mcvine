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
        outdir = 'out-component-calling-exit'
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        self.assertRaises(
            RuntimeError, mcvine.run_script.run1, 'test_component_calling_exit.py', outdir, 1
        )
        return

    pass  # end of TestCase


if __name__ == "__main__": unittest.main()

# End of file
