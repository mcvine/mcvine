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
    
    def test_band(self):
        "mcvine phonon band"
        cmd = "mcvine phonon band %s" % self.phonons_path
        os.system(cmd)
        return


if __name__ == '__main__': unittest.main()
