#!/usr/bin/env python
#

standalone = True

import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'

import mcni, shutil, numpy as np
from mccomponents.sample import samplecomponent


import unittest
class TestCase(unittest.TestCase):


    def test1a(self):
        "difference: two blocks"
        self._test('sampleassembly-variants/sampleassembly.xml.difference_of_two_blocks', (0., 0., -0.025), (.1, .1, .05))
        return

    def _test(self, xml, center, size):
        from utils import createSampleAssembly
        saxml = createSampleAssembly('.', './sampleassembly', xml)
        sample = samplecomponent( 'test', saxml)
        check(sample, center, size)
        import shutil
        shutil.rmtree(os.path.dirname(saxml))
        return
    
    pass  # end of TestCase


def check(sample, center, size):
    x0,y0,z0 = center
    x,y,z = size
    
    neutron = mcni.neutron(r=(x0,y0,z0-1), v=(0,0,1), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[2], z0+z/2., rtol=1e-3, atol=1e-6)

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
