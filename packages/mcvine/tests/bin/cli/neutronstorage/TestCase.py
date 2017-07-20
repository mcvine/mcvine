#!/usr/bin/env python

import unittest, os, sys
import mcvine, mcvine.resources
from mcni.neutron_storage.idf_usenumpy import count


class TestCase(unittest.TestCase):
    
    def test_count(self):
        "mcvine neutronstorage count"
        cmd = "mcvine neutronstorage count neutrons"
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        return

    def test_extract(self):
        "mcvine neutronstorage extract"
        cmd = "mcvine neutronstorage extract neutrons neutrons.extracted --start 0 --end 10"
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        assert count('neutrons.extracted')==10
        return

    def test_merge(self):
        "mcvine neutronstorage merge"
        if os.path.exists('merged_neutrons.1'): os.remove('merged_neutrons.1')
        cmd = "mcvine neutronstorage merge --files neutrons,neutrons --out merged_neutrons.1"
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        assert count('merged_neutrons.1')==2*count('neutrons')

        if os.path.exists('merged_neutrons.2'): os.remove('merged_neutrons.2')
        cmd = "mcvine neutronstorage extract neutrons neutrons.extracted-for-merge-test --start 0 --end 10"
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        cmd = "mcvine neutronstorage merge --files neutrons,neutrons.*-merge-test --out merged_neutrons.2"
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        assert count('merged_neutrons.2')==count('neutrons')+10
        return


if __name__ == '__main__': unittest.main()
