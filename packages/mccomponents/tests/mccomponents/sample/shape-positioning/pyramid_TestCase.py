#!/usr/bin/env python
#
#


import unittest, numpy as np


class TestCase(unittest.TestCase):


    def test1(self):
        'shape positioning: pyramid with vertical axis'
        # source
        from mcni.components.MonochromaticSource import MonochromaticSource
        import mcni
        neutron = mcni.neutron(r=(0,0.02,-1), v=(0,0,1000), prob=1)
        source = MonochromaticSource('s', neutron, dx=0.025, dy=0.012, dE=0)
        # sample
        from mccomponents.sample import samplecomponent
        scatterer = samplecomponent('sa', 'pyramid/sampleassembly.xml' )
        shape = scatterer.shape()
        from mccomposite import bindings; bpb = bindings.default()
        self.assertEqual(bpb.locate(bpb.position(0, -0.03, 0), shape), 'onborder')
        self.assertEqual(bpb.locate(bpb.position(0.0, 0.05-0.03, 0.0), shape), 'inside')
        self.assertEqual(bpb.locate(bpb.position(0.009, 0.001-0.03, 0.0045), shape), 'inside')
        self.assertEqual(bpb.locate(bpb.position(0.01, 0.001-0.03, 0.0045), shape), 'outside')
        self.assertEqual(bpb.locate(bpb.position(0., 0.0, 0.), shape), 'inside')

        # neutrons
        N = 100000
        neutrons = mcni.neutron_buffer(N)
        neutrons = source.process(neutrons)
        # find neutrons out of target
        arr = neutrons.to_npyarr()
        x,y,z = arr[:, :3].T
        missing = (y<-0.03) | (y>0.03) | (np.abs(x)>0.005-y/6.)
        # print neutrons
        scatterer.process(neutrons)
        # print neutrons
        arr = neutrons.to_npyarr()
        x,y,z = arr[:, :3].T
        assert (z[missing] < -.9).all()
        hit = arr[np.logical_not(missing), :3]
        x,y,z = hit.T
        assert (
            np.isclose( z+0.0025-y/0.03*0.0025, 0.) |
            np.isclose( z-0.0025+y/0.03*0.0025, 0.) |
            np.isclose( x+0.005-y/0.03*0.005, 0.) |
            np.isclose( x-0.005+y/0.03*0.005, 0.) |
            np.isclose( y + 0.03, 0.)
        ).all()
        return
    

    pass  # end of scattererxml_TestCase


def main():
    unittest.main()

if __name__ == "__main__": main()
    
# End of file 
