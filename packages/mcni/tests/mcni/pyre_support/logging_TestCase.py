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
        'mcni.pyre_support: journaling'
        import subprocess as sp
        cmd = "./journal_test_app.py"
        out = sp.check_output(cmd, stderr=sp.STDOUT, shell=True)

        expected = """DEBUG - hello"""
        print("out.decode()",out.decode())
        assert expected in out.decode()
        return


    pass  # end of TestCase


if __name__ == "__main__": unittest.main()

# End of file 
