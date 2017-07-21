#!/usr/bin/env python

import unittest, os, sys, subprocess as sp, shlex, numpy as np
import mcvine, mcvine.resources


class TestCase(unittest.TestCase):
    
    def test_info(self):
        "mcvine component info"
        cmds = [
            "mcvine component info --help",
            "mcvine component info Source_simple",
            "mcvine component info NDMonitor --args=x,y",
            "mcvine component info Source_simple --supplier=mcstas2 --category=sources",
            ]
        map(testcmd, cmds)
        return


def testcmd(cmd):
    if os.system(cmd):
        raise RuntimeError("%s failed" % cmd)

if __name__ == '__main__': unittest.main()
