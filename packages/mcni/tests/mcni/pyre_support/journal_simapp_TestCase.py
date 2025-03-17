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
        print('EROOROOOOORRR', out.decode())
        expected = """journal_test_sim_app.py:18:process
 -- source(info)
 -- loop #0
 """
        assert expected in out.decode()
        return
    
        
    pass  # end of TestCase


if __name__ == "__main__": unittest.main()

# End of file 
