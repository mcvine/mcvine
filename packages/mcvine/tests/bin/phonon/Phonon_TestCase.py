#!/usr/bin/env python

import unittest, os, sys
import mcvine, mcvine.resources


class TestCase(unittest.TestCase):
    
    def setUp(self):
        src = os.path.join(mcvine.resources.root(), 'samples', 'V', '300K')
        self.V_path = dest = 'V-300K'
        if not os.path.exists(dest):
            os.symlink(src, dest)
        self.phonons_path = os.path.join(self.V_path, 'phonons')
        self.xyz_path = os.path.join(self.V_path, 'V-primitive.xyz')
        self.out = "_out"
        if not os.path.exists(self.out):
            os.makedirs(self.out)
        return
    
    def test_band(self):
        "mcvine phonon band"
        cmd = "mcvine phonon band %s --start 0 0 0 --end 2.0736585172209856 0.0 2.0736585172209856 --cartesian --output %s/band-cartesian.png" % (self.phonons_path, self.out)
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)

        cmd = "mcvine phonon band %s --start 0 0 0 --end 1 0 0 --output %s/band-hkl.png" % (
            self.phonons_path, self.out)
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        return


    def test_slice(self):
        "mcvine phonon slice"
        cmd = "mcvine phonon slice %s %s --start 0 0 0 --end 1 0 0 --npts=1000 --Eaxis=0 30 .1 --outhist %s/slice-hkl.h5" % (self.xyz_path, self.phonons_path, self.out)
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        return


if __name__ == '__main__': unittest.main()
