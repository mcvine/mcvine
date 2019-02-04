#!/usr/bin/env python
#
#

import os, shutil, numpy as np
here = os.path.dirname(__file__)

import unittest

class TestCase(unittest.TestCase):


    def test1(self):
        outdir = 'testdata'
        from mcni import run_ppsd_in_parallel
        run_ppsd_in_parallel(os.path.join(outdir, 'post-processing-scripts'), nodes=2)
        return

    pass # end of TestCase


if __name__ == "__main__": unittest.main()
    
# End of file 
