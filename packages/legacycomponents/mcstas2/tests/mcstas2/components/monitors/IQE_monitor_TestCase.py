#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2009 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''
This test makes sure S(Q,E) monitor is reasonable.
It should show a evely distributed intensities in the S(Q,E) plot.
'''


skip = False
standalone = False

interactive = False


import unittestX as unittest
import os


componentname = 'IQE_monitor'
category = 'monitors'

class TestCase(unittest.TestCase):

    def test(self):
        "wrap IQE_monitor"
        
        from mcstas2 import componentfactory
        factory = componentfactory( category, componentname )

        Ei = 70
        Qmin=0; Qmax=13.; nQ=130
        Emin=-50; Emax=50.; nE=100
        
        component = factory(
            'component',
            Ei=Ei,
            Qmin=Qmin, Qmax=Qmax, nQ=nQ,
            Emin=Emin, Emax=Emax, nE=nE,
            max_angle_out_of_plane=30, min_angle_out_of_plane=-30,
            max_angle_in_plane=120, min_angle_in_plane=-30,
            filename = 'IQE.dat',
            )
        from mcni.SimulationContext import SimulationContext
        component.simulation_context = SimulationContext()
        component.simulation_context.overwrite_datafiles = True
        component.simulation_context.outputdir = "out-IQE_monitor"
        
        import mcni
        from mcni.utils import conversion as C
        neutrons = mcni.neutron_buffer( nQ*nE )
        import numpy as N
        count = 0
        for Q in N.arange(Qmin, Qmax, (Qmax-Qmin)/nQ):
            for E in N.arange(Emin,Emax,(Emax-Emin)/nE):
                Ef = Ei-E
                cosphi = (Ei+Ef-C.k2e(Q))/(2*N.sqrt(Ei)*N.sqrt(Ef))
                vf = C.e2v(Ef)
                vfz = vf*cosphi
                sinphi = N.sqrt(1-cosphi*cosphi)
                vfx = vf*sinphi
                neutrons[count] = mcni.neutron(r=(0,0,0), v=(vfx,0,vfz), time = 0, prob = 1)
                count += 1
            continue

        component.simulation_context.iteration_no = 0
        component.process( neutrons )
        
        import histogram.hdf as hh
        hist = hh.load(os.path.join(component.simulation_context.outputdir, 'step0', 'IQE.h5'))
        if interactive:
            from histogram.plotter import defaultPlotter
            defaultPlotter.plot(hist)
        return

    pass  # end of TestCase




def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    global interactive
    interactive = True
    main()
    
# version
__id__ = "$Id$"

# End of file 
