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
        'mcni.pyre_support: logging in instrument simulation app'
        import subprocess as sp
        cmd = "./logging_test_sim_app.py"
        out = sp.check_output(cmd, stderr=sp.STDOUT, shell=True)

        expected_loop0 = """INFO - loop #0"""
        expected_loop1 = """INFO - loop #1"""
        # print("out.decode()",out.decode())
        assert expected_loop0 in out.decode()
        assert expected_loop1 in out.decode()
        return


    pass  # end of TestCase


if __name__ == "__main__": unittest.main()

# End of file 