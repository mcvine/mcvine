#!/usr/bin/env python
#
#

standalone = True

import os, numpy as np
os.environ['MCVINE_MPI_BINDING'] = 'NONE'

import unittestX as unittest

class TestCase(unittest.TestCase):

    def test1(self):
        'mccomponents.sample.samplecomponent: SvQkernel'
        # The kernel spec is in sampleassemblies/V-svqkernel/V-scatterer.xml
        import mcni
        from mcni.utils import conversion
        # instrument
        # 1. source
        from mcni.components.MonochromaticSource import MonochromaticSource
        ei = 200.
        vil = conversion.e2v(ei)
        vi = (0,0,vil)
        neutron = mcni.neutron(r = (0,0,0), v = vi, time = 0, prob = 1 )
        component1 = MonochromaticSource('source', neutron)
        # 2. sample
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'sample', 'sampleassemblies/V-svqkernel/sampleassembly.xml' )
        # instrument and geometer
        instrument = mcni.instrument( [component1, component2, ] )
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,0) )
        # neutron buffer
        N0 = 100000
        neutrons = mcni.neutron_buffer(N0)
        #
        # simulate
        import mcni.SimulationContext
        workdir = "tmp.SvQkernel"
        if os.path.exists(workdir):
            import shutil; shutil.rmtree(workdir)
        sim_context = mcni.SimulationContext.SimulationContext(outputdir=workdir)
        mcni.simulate( instrument, geometer, neutrons, context=sim_context )
        return
        # to be worked on later
        # check  directly calculate I(Qx,Qy,Qz) from neutron buffer
        from mcni.neutron_storage import neutrons_as_npyarr
        narr = neutrons_as_npyarr(neutrons); narr.shape = N0, 10
        v = narr[:, 3:6]; p = narr[:, 9]
        delta_v_vec = -v + vi;
        Q_vec = conversion.V2K * delta_v_vec
        Qxbins = np.arange(-10, 10, .2)
        Qybins = np.arange(-10, 11, .2)
        Qzbins = np.arange(-10, 12, .2)
        bins = Qxbins, Qybins, Qzbins
        I, (qxbb, qybb, qzbb) = np.histogramdd(Q_vec, bins, weights=p)
        qxc = (qxbb[1:] + qxbb[:-1])/2
        qyc = (qybb[1:] + qybb[:-1])/2
        qzc = (qzbb[1:] + qzbb[:-1])/2
        from matplotlib import pyplot as plt
        plt.figure()
        qxg, qyg = np.meshgrid(qxc, qyc)
        plt.pcolormesh(qxg, qyg, I[:, :, 50].T)
        plt.colorbar()
        plt.show()
        return

    pass  # end of TestCase

if __name__ == "__main__": unittest.main()

# End of file 
