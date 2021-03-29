#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


import os

import unittest

class TestCase(unittest.TestCase):

    def test1(self):
        import mcpl
        fn = ...
        myfile = mcpl.MCPLFile(fn)
        pbs = myfile.particle_blocks
        for p in myfile.particle_blocks:
            print( p.x, p.y, p.z, p.time, p.weight, p.direction, p.ekin )
        return

    pass  # end of TestCase

if __name__ == "__main__": unittest.main()
# End of file
