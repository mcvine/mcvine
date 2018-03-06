#!/usr/bin/env python
#

standalone = True

import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'

import mcni, shutil, numpy as np
from mccomponents.sample import samplecomponent


r0, r1, h = 0.02, 0.03, 0.2
rm = (r0+r1)/2.
s45 = np.sin(np.pi/4)


import unittest
class TestCase(unittest.TestCase):


    def test1a(self):
        # hollow cylinder is along beam
        xml = 'sampleassembly-variants/sampleassembly.xml.rot_x90_hollow_cyl'
        from utils import createSampleAssembly
        saxml = createSampleAssembly('.', './sampleassembly', xml)
        sample = samplecomponent( 'test', saxml)

        # neutrons moving vertically up, perpendicular to the cylinder
        neutron = mcni.neutron(r=(0, -1, 0), v=(0,1,0), prob=1.)
        sample.scatter(neutron)
        assert np.isclose(neutron.state.position[1], r1)

        neutron = mcni.neutron(r=(0.5*r1, -1, 0), v=(0,1,0), prob=1.)
        sample.scatter(neutron)
        assert np.allclose(neutron.state.position, [.5*r1, .5*3**.5*r1, 0])

        # neutrons moving horizontally, perpendicular to the cylinder
        neutron = mcni.neutron(r=(-1, 0, 0), v=(1,0,0), prob=1.)
        sample.scatter(neutron)
        assert np.isclose(neutron.state.position[0], r1)

        neutron = mcni.neutron(r=(-1, 0.5*r1, 0), v=(1,0,0), prob=1.)
        sample.scatter(neutron)
        assert np.allclose(neutron.state.position, [.5*3**.5*r1, .5*r1, 0])

        # neutron moving along beam direction
        # through the hole
        neutron = mcni.neutron(r=(0, 0, -1), v=(0,0,1), prob=1.)
        sample.scatter(neutron)
        assert np.allclose(neutron.state.position, [0,0,-1])

        # hit the side
        neutron = mcni.neutron(r=(rm, 0, -1), v=(0,0,1), prob=1.)
        sample.scatter(neutron)
        assert np.allclose(neutron.state.position, [rm,0,h/2])

        neutron = mcni.neutron(r=(rm*s45, rm*s45, -1), v=(0,0,1), prob=1.)
        sample.scatter(neutron)
        assert np.allclose(neutron.state.position, [rm*s45,rm*s45,h/2])
        
        import shutil
        shutil.rmtree(os.path.dirname(saxml))
        return

    pass  # end of TestCase


def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
