#!/usr/bin/env python
#
#


standalone = True

import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'

import unittestX as unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.samplecomponent: SQkernel'
        import mcni
        from mcni.utils import conversion

        ei = 60
        vil = conversion.e2v(ei)
        vi = (0,0,vil)
        neutron = mcni.neutron(r = (0,0,0), v = vi, time = 0, prob = 1 )
        
        from mcni.components.MonochromaticSource import MonochromaticSource
        component1 = MonochromaticSource('source', neutron)
        
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'sample', 'sampleassemblies/V-sqkernel/sampleassembly.xml' )

        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,0) )

        N0 = 1000
        neutrons = mcni.neutron_buffer(N0)

        mcni.simulate( instrument, geometer, neutrons )
        return
    

    pass  # end of TestCase


    
if __name__ == "__main__": unittest.main()

    
# End of file 
