#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


standalone = True

import os
os.environ['MCVINE_MPI_LAUNCHER'] = 'serial'


import unittestX as unittest

class TestCase(unittest.TestCase):


    def test(self):
        'mcni.pyre_support: journaling in instrument simulation app'
        import subprocess as sp
        cmd = "./journal_test_sim_app.py --journal.info.source --ncount=2"
        out = sp.check_output(cmd, stderr=sp.STDOUT, shell=True)

        expected_loop0 = """./journal_test_sim_app.py:18:process\n -- source(info)\n -- loop #0"""
        expected_loop1 = """./journal_test_sim_app.py:18:process\n -- source(info)\n -- loop #1"""
        print("out.decode()",out.decode())
        assert expected_loop0 in out.decode()
        assert expected_loop1 in out.decode()
        return
    
        
    pass  # end of TestCase


if __name__ == "__main__": unittest.main()

# End of file 
