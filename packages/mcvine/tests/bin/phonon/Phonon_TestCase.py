#!/usr/bin/env python

import unittest, os, sys
import mcvine, mcvine.resources


class TestCase(unittest.TestCase):
    
    def setUp(self):
        src = os.path.join(mcvine.resources.root(), 'samples', 'V', '300K', 'phonons')
        self.phonons_path = dest = 'V-phonons'
        if not os.path.exists(dest):
            os.symlink(src, dest)
        return
    
    def _test_band(self):
        "mcvine phonon band"
        cmd = "mcvine phonon band %s --start 0 0 0 --end 2.0736585172209856 0.0 2.0736585172209856 --cartesian --output band-cartesian.png" % self.phonons_path
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)

        cmd = "mcvine phonon band %s --start 0 0 0 --end 1 0 0 --output band-hkl.png" % self.phonons_path
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        return


    def test_slice(self):
        "mcvine phonon slice"
        cmd = "mcvine phonon slice %s --start 0 0 0 --end 1 0 0 --npts=1000 --output slice-hkl.png" % self.phonons_path
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        return


if __name__ == '__main__': unittest.main()
