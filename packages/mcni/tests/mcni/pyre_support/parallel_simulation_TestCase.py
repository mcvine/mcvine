#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

standalone = True


import unittest
import journal

debug = journal.debug( "mcni.pyre_support.test" )
warning = journal.warning( "mcni.pyre_support.test" )


class TestCase(unittest.TestCase):


    def test(self):
        'mcni.pyre_support: parallel simulation'
        from mcni.pyre_support.MpiApplication import mpi_launcher_choice as launcher
        cmd = "python parallel_simulation_demoapp.py --%s.nodes=2" % launcher
        import os
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        return
        
    pass  # end of TestCase


if __name__ == "__main__":  unittest.main()

# End of file 
