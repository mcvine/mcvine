#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import unittestX as unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.samplecomponent: IsotropicKernel'
        import mcni
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,3000), time = 0, prob = 1 )
        from mcni.components.MonochromaticSource import MonochromaticSource
        component1 = MonochromaticSource('source', neutron)
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'Al', 'sampleassembly/Al-isotropickernel.xml' )
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,0) )

        N0 = 1000
        neutrons = mcni.neutron_buffer(N0)

        mcni.simulate( instrument, geometer, neutrons )

        N = len(neutrons)

        for i in range(10):
            neutron = neutrons[i]
            print neutron
            continue

        # N should be about 2/3 of N0. this is determined by
        # the mc weights in Al-isotropic-kernel-plate-scatterer.xml
        self.assert_( N < 0.72*N0 and N > 0.6*N0)

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
