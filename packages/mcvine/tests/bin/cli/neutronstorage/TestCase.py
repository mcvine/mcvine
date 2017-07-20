#!/usr/bin/env python

import unittest, os, sys
import mcvine, mcvine.resources


class TestCase(unittest.TestCase):
    
    def test_count(self):
        "mcvine neutronstorage count"
        cmd = "mcvine neutronstorage count neutrons"
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        return


if __name__ == '__main__': unittest.main()
