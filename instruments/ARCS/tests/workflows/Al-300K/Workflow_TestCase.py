#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

import mcvine, mcvine.resources
import os, shutil

import unittest
class TestCase(unittest.TestCase):

    def test(self):
        "ARCS Al 300K simulation workflow"
        src = os.path.join(mcvine.resources.instrument('ARCS'), 'simulations/aluminum/plate-rotated28deg-Ei80meV')
        dest = os.path.join("work")
        shutil.copytree(src, dest)
        return


if __name__ == '__main__': unittest.main()

# End of file 
