#!/usr/bin/env python

import unittest, os, sys, subprocess as sp, shlex, numpy as np
import mcvine, mcvine.resources


class TestCase(unittest.TestCase):
    
    def test_info(self):
        "mcvine mcstas compilecomponent"
        cmds = [
            "mcvine mcstas compilecomponent --help",
            # "mcvine mcstas compilecomponent --filename=Al_window.comp --category=optics"
            ]
        map(testcmd, cmds)
        return


def testcmd(cmd):
    if os.system(cmd):
        raise RuntimeError("%s failed" % cmd)

if __name__ == '__main__': unittest.main()
