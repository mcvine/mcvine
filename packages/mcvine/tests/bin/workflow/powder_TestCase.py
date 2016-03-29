#!/usr/bin/env python

import unittest, os, sys, shutil


class TestCase(unittest.TestCase):
    
    def test(self):
        "mcvine workflow powder"
        cmd = "mcvine workflow powder"
        if os.system(cmd): raise RuntimeError("%s failed" % cmd)
        wfdir = "mcvine-workflow-powder-ARCS-V"
        assert os.path.exists(wfdir) and os.path.isdir(wfdir)
        shutil.rmtree(wfdir)
        return


if __name__ == '__main__': unittest.main()
