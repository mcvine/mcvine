#!/usr/bin/env python
#

standalone = True

import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'

import mcni, shutil, numpy as np
from mccomponents.sample import samplecomponent


thickness, width, height = 0.01, 0.06, 0.1


import unittest
class TestCase(unittest.TestCase):


    def test1(self):
        "no rotation"
        self._test('sampleassembly/sampleassembly.xml.no-rotation', width, height, thickness)
        return

    def test2a(self):
        "rotation: 90deg about x"
        self._test('sampleassembly/sampleassembly.xml.rot_x90', width, thickness, height)
        return

    def test2b(self):
        "rotation: 90deg about y"
        self._test('sampleassembly/sampleassembly.xml.rot_y90', thickness, height, width)
        return

    def test2c(self):
        "rotation: 90deg about z"
        self._test('sampleassembly/sampleassembly.xml.rot_z90', height, width, thickness)
        return

    def test2d(self):
        "rotation: 90deg about x, 90deg about y'"
        self._test('sampleassembly/sampleassembly.xml.rot_x90y90', thickness, width, height)
        return

    def test3a(self):
        "orientation: 90deg about x"
        self._test('sampleassembly/sampleassembly.xml.orientation_90,0,0', height, width, thickness)
        return

    def test3b(self):
        "orientation: 90deg about y"
        self._test('sampleassembly/sampleassembly.xml.orientation_0,90,0', width, thickness, height)
        return

    def test3a(self):
        "orientation: 90deg about z"
        self._test('sampleassembly/sampleassembly.xml.orientation_0,0,90', thickness, height, width)
        return

    def test3d(self):
        "orientation: 90deg about x, 90deg about y"
        self._test('sampleassembly/sampleassembly.xml.orientation_90,90,0', height, thickness, width)
        return

    def test4a(self):
        "orientation: 90deg about x. mcstas convention"
        self._test('sampleassembly/sampleassembly.xml.orientation_mcstas_90,0,0', width, thickness, height)
        return

    def test4b(self):
        "orientation: 90deg about y. mcstas convention"
        self._test('sampleassembly/sampleassembly.xml.orientation_mcstas_0,90,0', thickness, height, width)
        return

    def test4c(self):
        "orientation: 90deg about z. mcstas convention"
        self._test('sampleassembly/sampleassembly.xml.orientation_mcstas_0,0,90', height, width, thickness)
        return

    def test4d(self):
        "orientation: 90deg about x, 90deg about y'. mcstas convention"
        self._test('sampleassembly/sampleassembly.xml.orientation_mcstas_90,90,0', thickness, width, height)
        return

    def _test(self, xml, x, y, z):
        shutil.copyfile(xml, 'sampleassembly/sampleassembly.xml')
        sample = samplecomponent( 'test', 'sampleassembly/sampleassembly.xml' )
        check(sample, x, y, z)
        return
    
    pass  # end of TestCase


def check(sample, x, y, z):
    neutron = mcni.neutron(r=(0,0,-1), v=(0,0,1), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[2], z/2.)

    neutron = mcni.neutron(r=(0,0,1), v=(0,0,-1), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[2], -z/2.)

    neutron = mcni.neutron(r=(0,-1,0), v=(0,1,0), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[1], y/2.)

    neutron = mcni.neutron(r=(0,1,0), v=(0,-1,0), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[1], -y/2.)

    neutron = mcni.neutron(r=(-1,0,0), v=(1,0,0), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[0], x/2.)

    neutron = mcni.neutron(r=(1,0,0), v=(-1,0,0), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[0], -x/2.)
    return

def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
