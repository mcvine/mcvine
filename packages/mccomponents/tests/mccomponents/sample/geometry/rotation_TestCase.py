#!/usr/bin/env python
#

standalone = True

import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'

import mcni, shutil, numpy as np


import unittest
class TestCase(unittest.TestCase):


    def test1(self):
        from mccomponents.sample import samplecomponent
        shutil.copyfile('sampleassembly/sampleassembly.xml.no-rotation', 'sampleassembly/sampleassembly.xml')
        thickness, width, height = 0.01, 0.06, 0.1
        
        sample = samplecomponent( 'test', 'sampleassembly/sampleassembly.xml' )
        check(sample, width, height, thickness)

        shutil.copyfile('sampleassembly/sampleassembly.xml.rot_x90', 'sampleassembly/sampleassembly.xml')
        sample = samplecomponent( 'test', 'sampleassembly/sampleassembly.xml' )
        check(sample, width, thickness, height)

        shutil.copyfile('sampleassembly/sampleassembly.xml.rot_y90', 'sampleassembly/sampleassembly.xml')
        sample = samplecomponent( 'test', 'sampleassembly/sampleassembly.xml' )
        check(sample, thickness, height, width)

        shutil.copyfile('sampleassembly/sampleassembly.xml.rot_z90', 'sampleassembly/sampleassembly.xml')
        sample = samplecomponent( 'test', 'sampleassembly/sampleassembly.xml' )
        check(sample, height, width, thickness)
        return
    

    pass  # end of TestCase

def check(sample, x, y, z):
    neutron = mcni.neutron(r=(0,0,-1), v=(0,0,1), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[2], z/2.)

    neutron = mcni.neutron(r=(0,-1,0), v=(0,1,0), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[1], y/2.)

    neutron = mcni.neutron(r=(-1,0,0), v=(1,0,0), prob=1.)
    sample.scatter(neutron)
    assert np.isclose(neutron.state.position[0], x/2.)
    return

def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
