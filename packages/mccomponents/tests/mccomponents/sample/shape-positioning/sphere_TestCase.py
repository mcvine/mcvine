#!/usr/bin/env python
#
#


import unittest, numpy as np


class TestCase(unittest.TestCase):


    def test1(self):
        'shape positioning: sphere'
        # source
        from mcni.components.MonochromaticSource import MonochromaticSource
        import mcni
        neutron = mcni.neutron(r=(0,0,-1), v=(0,0,1000), prob=1)
        source = MonochromaticSource('s', neutron, dx=0.10, dy=0.09, dE=0)
        # sample
        from mccomponents.sample import samplecomponent
        scatterer = samplecomponent('sa', 'sphere/sampleassembly.xml' )
        # neutrons
        N = 1000
        neutrons = mcni.neutron_buffer(N)
        neutrons = source.process(neutrons)
        # find neutrons out of target
        arr = neutrons.to_npyarr()
        x,y,z = arr[:, :3].T
        missing = x*x+y*y>0.05*0.05
        # print "missed:", missing.sum()
        # print neutrons
        scatterer.process(neutrons)
        # print neutrons
        arr = neutrons.to_npyarr()
        x,y,z = arr[:, :3].T
        assert (z[missing] < -.9).all()
        hit = arr[np.logical_not(missing), :3]
        x,y,z = hit.T
        assert (z > -.1).all()
        assert np.isclose(np.abs(x*x+y*y+z*z), 0.05*0.05).all()
        return
    

    def test2(self):
        'shape positioning: rotated sphere'
        # source
        from mcni.components.MonochromaticSource import MonochromaticSource
        import mcni
        neutron = mcni.neutron(r=(0,0,-1), v=(0,0,1000), prob=1)
        source = MonochromaticSource('s', neutron, dx=0.10, dy=0.09, dE=0)
        # sample
        from mccomponents.sample import samplecomponent
        scatterer = samplecomponent('sa', 'sphere-rotated-arbitrarily/sampleassembly.xml' )
        # neutrons
        N = 1000
        neutrons = mcni.neutron_buffer(N)
        neutrons = source.process(neutrons)
        # find neutrons out of target
        arr = neutrons.to_npyarr()
        x,y,z = arr[:, :3].T
        missing = x*x+y*y>0.05*0.05
        # print "missed:", missing.sum()
        # print neutrons
        scatterer.process(neutrons)
        # print neutrons
        arr = neutrons.to_npyarr()
        x,y,z = arr[:, :3].T
        assert (z[missing] < -.9).all()
        hit = arr[np.logical_not(missing), :3]
        x,y,z = hit.T
        assert (z > -.1).all()
        assert np.isclose(np.abs(x*x+y*y+z*z), 0.05*0.05).all()
        return
    

    pass  # end of scattererxml_TestCase


def main(): unittest.main()

if __name__ == "__main__": main()
    
# End of file 
