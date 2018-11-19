#!/usr/bin/env python
#
#


standalone = True

import os, numpy as np
os.environ['MCVINE_MPI_BINDING'] = 'NONE'

import unittestX as unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.samplecomponent: SQkernel'
        import mcni
        from mcni.utils import conversion
        # instrument
        # 1. source
        from mcni.components.MonochromaticSource import MonochromaticSource
        ei = 60.
        vil = conversion.e2v(ei)
        vi = (0,0,vil)
        neutron = mcni.neutron(r = (0,0,0), v = vi, time = 0, prob = 1 )
        component1 = MonochromaticSource('source', neutron)
        # 2. sample
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'sample', 'sampleassemblies/V-sqkernel/sampleassembly.xml' )
        # 3. monitor
        import mcstas2
        component3 = mcstas2.componentfactory('monitors', 'IQE_monitor')(
            name='monitor', Ei=ei, Qmin=0, Qmax=8., Emin=-10., Emax=10., nQ=20, nE=20)
        # instrument and geometer
        instrument = mcni.instrument( [component1, component2, component3] )
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,0) )
        geometer.register( component3, (0,0,1), (0,0,0) )
        # neutron buffer
        N0 = 500000
        neutrons = mcni.neutron_buffer(N0)
        #
        # simulate
        import mcni.SimulationContext
        workdir = "tmp.SQkernel"
        if os.path.exists(workdir):
            import shutil; shutil.rmtree(workdir)
        sim_context = mcni.SimulationContext.SimulationContext(outputdir=workdir)
        mcni.simulate( instrument, geometer, neutrons, context=sim_context )
        #
        # check 1: directory calculate I(Q) from neutron buffer
        from mcni.neutron_storage import neutrons_as_npyarr
        narr = neutrons_as_npyarr(neutrons); narr.shape = N0, 10
        v = narr[:, 3:6]; p = narr[:, 9]
        delta_v_vec = -v + vi; delta_v = np.linalg.norm(delta_v_vec, axis=-1)
        Q = conversion.V2K * delta_v
        I, qbb = np.histogram(Q, 20, weights=p)
        qbc = (qbb[1:] + qbb[:-1])/2
        I=I/qbc; I/=I[0]
        self.assert_(np.allclose(I, 1., atol=0.1))
        #
        # check 2: use data in IQE monitor
        import histogram.hdf as hh
        iqe = hh.load(os.path.join(workdir, 'stepNone', 'iqe_monitor.h5'))
        iq = iqe.sum('energy')
        Q = iq.Q; I = iq.I
        I0 = I[0]
        self.assert_(np.allclose(I/I0, 1., atol=0.15))  # see sampleassemblies/V-sqkernel/V-scatterer.xml
        return
    

    pass  # end of TestCase


    
if __name__ == "__main__": unittest.main()

    
# End of file 
