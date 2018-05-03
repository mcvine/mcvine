#!/usr/bin/env python
#
#


import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'


import unittest


class TestCase(unittest.TestCase):


    def test1(self):
        import mcvine.run_script
        mcvine.run_script.run1('test_instrument.py', 'out-run1_TestCase', 1e5, overwrite_datafiles=True)
        return

    
    pass  # end of TestCase



if __name__ == "__main__": unittest.main()
    
# End of file 
