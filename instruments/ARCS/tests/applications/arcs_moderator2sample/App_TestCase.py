#!/usr/bin/env python
#

import os, subprocess as sp, shlex
from mcvine.resources import instrument

cwd = os.path.abspath(os.path.dirname(__file__))

import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        source_file = os.path.join(instrument('ARCS'), "moderator/source_sct521_bu_17_1.dat")
        from mcni.pyre_support.MpiApplication \
            import mpi_launcher_choice as launcher
        cmd = "mcvine instruments arcs mod2sample --moderator.S_filename=%s --ncount=1e5 --buffer_size=10000 --%s.nodes=2" % (source_file, launcher)
        sp.check_call(shlex.split(cmd), shell=False, cwd=cwd)
        return


    pass  # end of TestCase



def main(): unittest.main()
if __name__ == "__main__":  main()
    
# End of file 
