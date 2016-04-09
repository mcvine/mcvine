#!/usr/bin/env python
#

import subprocess as sp, os, shlex


import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        cmd = 'mcvine instruments arcs m2s --E=100 --with_moderator_angling=no --- --dump-pml=yes -h'
        workdir = os.path.abspath(os.path.dirname(__file__))
        sp.check_call(
            shlex.split(cmd),
            shell=False, cwd=workdir)
        return


    pass  # end of TestCase



def main(): unittest.main()
if __name__ == "__main__":
    main()
    
# End of file 
