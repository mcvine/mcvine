#!/usr/bin/env python
#
#


import os
import mcvine.run_script

import unittest
class TestCase(unittest.TestCase):


    def test1(self):
        mcvine.run_script.run1('test_instrument.py', 'out-run1', 1e5, overwrite_datafiles=True)
        return

    
    def test2(self):
        mcvine.run_script.run1_mpi('test_instrument.py', 'out-run1_mpi', 1e5, overwrite_datafiles=True)
        return

    
    def test3(self):
        mcvine.run_script.run_mpi('test_instrument.py', 'out-run_mpi', 1e5, nodes=2, overwrite_datafiles=True)
        return

    
    pass  # end of TestCase



if __name__ == "__main__": unittest.main()
    
# End of file 
