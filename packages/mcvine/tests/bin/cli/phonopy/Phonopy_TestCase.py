#!/usr/bin/env python

import unittest, os, sys
import mcvine, mcvine.resources


class TestCase(unittest.TestCase):
    
    def setUp(self):
        src = os.path.join(mcvine.resources.root(), 'samples', 'Si', '100K')
        self.Si_path = dest = 'Si-100K'
        if not os.path.exists(dest):
            os.symlink(src, dest)
        self.phonons_path = os.path.join(self.Si_path, 'phonons', 'vasp-phonopy')
        self.out = "_out"
        if not os.path.exists(self.out):
            os.makedirs(self.out)
        return
    
    def test(self):
        "mcvine phonopy griddisp"
        cmd = "mcvine phonopy griddisp "
        options = {
            'force-constants': os.path.join(self.phonons_path, 'FORCE_CONSTANTS'),
            'poscar': os.path.join(self.phonons_path, 'POSCAR'),
            'species': 'Si',
            'supercell-dims': '5 5 5',
            'qgrid-dims': '51 51 51',
            }
        cmd += ' '.join('--%s %s' % (k, v) for k,v in options.items())
        print cmd
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        return


if __name__ == '__main__': unittest.main()
