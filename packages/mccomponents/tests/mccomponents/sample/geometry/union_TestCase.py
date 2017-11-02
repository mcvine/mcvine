#!/usr/bin/env python
#

standalone = True

import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'

import mcni, shutil, numpy as np
from mccomponents.sample import samplecomponent


r, h = 0.01, 0.08
thickness, width, height = 0.001, 0.05, 0.1


import unittest
class TestCase(unittest.TestCase):


    def test1a(self):
        xml = 'sampleassembly/sampleassembly.xml.union_of_plate_cylinder'
        shutil.copyfile(xml, 'sampleassembly/sampleassembly.xml')
        sample = samplecomponent( 'test', 'sampleassembly/sampleassembly.xml' )

        # neutrons moving along beam direction
        neutron = mcni.neutron(r=(0, 0, -1), v=(0,0,1), prob=1.)
        sample.scatter(neutron)
        assert np.allclose(neutron.state.position, (0, 0, r))

        # neutrons moving along beam direction, starting from a higher position to avoid the cylinder 
        neutron = mcni.neutron(r=(0, (h+height)/4, -1), v=(0,0,1), prob=1.)
        sample.scatter(neutron)
        assert np.allclose(neutron.state.position, (0, (h+height)/4, thickness/2))

        # neutrons moving along beam direction, starting from a left position to avoid the cylinder 
        neutron = mcni.neutron(r=((r+width/2)/2, 0, -1), v=(0,0,1), prob=1.)
        sample.scatter(neutron)
        assert np.allclose(neutron.state.position, ((r+width/2)/2, 0, thickness/2))
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
