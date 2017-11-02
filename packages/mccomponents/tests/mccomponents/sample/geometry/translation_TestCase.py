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


    def test1a(self):
        "translation: (1,0,0)"
        self._test('sampleassembly/sampleassembly.xml.mov_1,0,0', (1., 0., 0.), (width, height, thickness))
        return

    def test1b(self):
        "translation: (0,1,0)"
        self._test('sampleassembly/sampleassembly.xml.mov_0,1,0', (0., 1., 0.), (width, height, thickness))
        return

    def test1c(self):
        "translation: (0,0,1)"
        self._test('sampleassembly/sampleassembly.xml.mov_0,0,1', (0., 0., 1.), (width, height, thickness))
        return


    def _test(self, xml, center, size):
        shutil.copyfile(xml, 'sampleassembly/sampleassembly.xml')
        sample = samplecomponent( 'test', 'sampleassembly/sampleassembly.xml' )
        check(sample, center, size)
        return
    
    pass  # end of TestCase


def check(sample, center, size):
    x0,y0,z0 = center
    x,y,z = size
    
    neutron = mcni.neutron(r=(x0,y0,z0-1), v=(0,0,1), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[2], z0+z/2.)

    neutron = mcni.neutron(r=(x0,y0,z0+1), v=(0,0,-1), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[2], z0-z/2.)

    neutron = mcni.neutron(r=(x0,y0-1,z0), v=(0,1,0), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[1], y0+y/2.)

    neutron = mcni.neutron(r=(x0,y0+1,z0), v=(0,-1,0), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[1], y0-y/2.)

    neutron = mcni.neutron(r=(x0-1,y0,z0), v=(1,0,0), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[0], x0+x/2.)

    neutron = mcni.neutron(r=(x0+1,y0,z0), v=(-1,0,0), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[0], x0-x/2.)
    return

def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
