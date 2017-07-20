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

    def test_extract(self):
        "mcvine neutronstorage extract"
        cmd = "mcvine neutronstorage extract neutrons neutrons2 --start 0 --end 10"
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        from mcni.neutron_storage.idf_usenumpy import count
        assert count('neutrons2')==10
        return


if __name__ == '__main__': unittest.main()
