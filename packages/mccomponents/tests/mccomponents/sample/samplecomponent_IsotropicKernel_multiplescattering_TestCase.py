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


standalone = True

import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'


import unittestX as unittest
import journal

debug = journal.debug( "samplecomponent_TestCase" )
warning = journal.warning( "samplecomponent_TestCase" )


scattererxml = 'Ni-scatterer.xml'


class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.samplecomponent isotropic kernel, multiple-scattering'
        import mcni
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,3000), time = 0, prob = 1 )
        from mcni.components.MonochromaticSource import MonochromaticSource
        component1 = MonochromaticSource('source', neutron)
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'Al', 'sampleassemblies/Al-isotropickernel/sampleassembly.xml' )
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,0) )

        N0 = 1
        neutrons = mcni.neutron_buffer(N0)

        mcni.simulate( instrument, geometer, neutrons, multiple_scattering=True)

        N = len(neutrons)

        for i in range(N):
            neutron = neutrons[i]
            print(neutron)
            continue

        return
    

    pass  # end of TestCase


def main():
    import journal
    journal.debug('CompositeNeutronScatterer_Impl').activate()
    journal.debug('HomogeneousNeutronScatterer').activate()
    journal.debug('IsotropicKernel').activate()
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
