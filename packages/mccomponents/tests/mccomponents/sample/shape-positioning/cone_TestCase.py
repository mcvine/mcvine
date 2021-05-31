#!/usr/bin/env python
#
#


import unittest, numpy as np


class TestCase(unittest.TestCase):


    def test1(self):
        'shape positioning: cone with vertical axis'
        # source
        from mcni.components.MonochromaticSource import MonochromaticSource
        import mcni
        neutron = mcni.neutron(r=(0,0.,-1), v=(0,0,1000), prob=1)
        source = MonochromaticSource('s', neutron, dx=0.04, dy=0.07, dE=0)
        # sample
        from mccomponents.sample import samplecomponent
        scatterer = samplecomponent('sa', 'cone/sampleassembly.xml' )
        shape = scatterer.shape()
        from mccomposite import bindings; bpb = bindings.default()
        self.assertEqual(bpb.locate(bpb.position(0, -0.03, 0), shape), 'onborder')
        self.assertEqual(bpb.locate(bpb.position(0.0, 0.05-0.03, 0.0), shape), 'inside')
        self.assertEqual(bpb.locate(bpb.position(0.02*.99*0.6, 0.00001-0.03, 0.02*.99*.8), shape), 'inside')
        self.assertEqual(bpb.locate(bpb.position(0.02*1.01*0.6, 0.00001-0.03, 0.02*1.01*.8), shape), 'outside')
        self.assertEqual(bpb.locate(bpb.position(0.01*0.99*.6, 0.03-0.03, 0.01*0.99*.8), shape), 'inside')
        self.assertEqual(bpb.locate(bpb.position(0.01*1.01*.6, 0.03-0.03, 0.01*1.01*.8), shape), 'outside')
        self.assertEqual(bpb.locate(bpb.position(0., 0.0, 0.), shape), 'inside')

        # neutrons
        N = 100000
        neutrons = mcni.neutron_buffer(N)
        neutrons = source.process(neutrons)
        # find neutrons out of target
        arr = neutrons.to_npyarr()
        x,y,z = arr[:, :3].T
        missing = (y<-0.03) | (y>0.03) | (np.abs(x)>0.01-y/3.)
        # print neutrons
        scatterer.process(neutrons)
        # print neutrons
        arr = neutrons.to_npyarr()
        x,y,z = arr[:, :3].T
        z1 = z[missing]
        print(z1[z1>=-0.9])
        assert (z1>=-0.0).sum() < 1e-4*N
        hit = arr[np.logical_not(missing), :3]
        x,y,z = hit.T
        condition = np.isclose( x*x + z*z, (0.01-y/3)**2 ) | np.isclose( y + 0.03, 0.)
        print(np.sum(condition), len(hit))
        assert np.sum(condition)>.99*len(hit)
        return

    pass  # end of scattererxml_TestCase


def main(): unittest.main()

if __name__ == "__main__": main()

# End of file
