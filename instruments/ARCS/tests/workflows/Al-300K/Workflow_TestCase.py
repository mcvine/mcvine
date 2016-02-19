#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

import mcvine, mcvine.resources
import os, shutil, subprocess as sp

import unittest
class TestCase(unittest.TestCase):

    def test(self):
        "ARCS Al 300K simulation workflow"
        # copy template
        src = os.path.join(mcvine.resources.instrument('ARCS'), 'simulations/aluminum/plate-rotated28deg-Ei80meV')
        workdir = "work"
        dest = os.path.join(workdir)
        shutil.rmtree(dest)
        shutil.copytree(src, dest)
        # run 
        from mcvine.instruments.ARCS.applications.utils import execute
        execute("make", workdir)
        # generate a plot
        cmd = "PlotHist.py --min=0 --max=0.001 --output=iqe.eps %s/iqe.h5" % workdir
        execute(cmd, os.curdir)
        return


if __name__ == '__main__': unittest.main()

# End of file 
