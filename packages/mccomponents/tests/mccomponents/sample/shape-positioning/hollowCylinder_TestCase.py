#!/usr/bin/env python
#
#


import unittest, numpy as np


class TestCase(unittest.TestCase):


    def test1(self):
        'shape positioning: hollow cylinder'
        # source
        from mcni.components.MonochromaticSource import MonochromaticSource
        import mcni
        neutron = mcni.neutron(r=(0,0,-1), v=(0,0,1000), prob=1)
        source = MonochromaticSource('s', neutron, dx=0.05, dy=0.07, dE=0)
        # sample
        from mccomponents.sample import samplecomponent
        scatterer = samplecomponent('sa', 'hollow-cyl/sampleassembly.xml' )
        # neutrons
        N = 1000
        neutrons = mcni.neutron_buffer(N)
        neutrons = source.process(neutrons)
        # find neutrons out of target
        arr = neutrons.to_npyarr()
        x,y,z = arr[:, :3].T
        missing = (x>0.02) | (x<-0.02) | (y>0.03) | (y<-0.03)
        # print neutrons
        scatterer.process(neutrons)
        # print neutrons
        arr = neutrons.to_npyarr()
        x,y,z = arr[:, :3].T
        assert (z[missing] < -.9).all()
        hit = arr[np.logical_not(missing), :3]
        x,y,z = hit.T
        assert (np.isclose((x*x + z*z)**.5, 0.02) 
                | np.isclose((x*x + z*z)**.5, 0.01)
                | np.isclose(np.abs(y), 0.03)).all()
        return
    

    pass  # end of scattererxml_TestCase


def main(): unittest.main()

if __name__ == "__main__": main()
    
# End of file 
