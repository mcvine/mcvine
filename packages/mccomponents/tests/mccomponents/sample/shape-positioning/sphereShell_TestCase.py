#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

import unittest, numpy as np

class TestCase(unittest.TestCase):

    def test1(self):
        'shape positioning: hollow cylinder'
        # source
        from mcni.components.MonochromaticSource import MonochromaticSource
        import mcni
        neutron = mcni.neutron(r=(0,0,0), v=(0,0,1000), prob=1)
        source = MonochromaticSource('s', neutron, dx=0.01, dy=0.015, dE=0)
        # sample
        from mccomponents.sample import samplecomponent
        scatterer = samplecomponent('sa', 'sphere-shell/sampleassembly.xml' )
        # neutrons
        N = 1000
        neutrons = mcni.neutron_buffer(N)
        neutrons = source.process(neutrons)
        # print neutrons
        scatterer.process(neutrons)
        # print neutrons
        arr = neutrons.to_npyarr()
        x,y,z = arr[:, :3].T
        assert np.allclose((x*x + y*y + z*z)**.5, 0.10)
        return

    pass  # end of scattererxml_TestCase


def main(): unittest.main()

if __name__ == "__main__": main()
    
# End of file 
