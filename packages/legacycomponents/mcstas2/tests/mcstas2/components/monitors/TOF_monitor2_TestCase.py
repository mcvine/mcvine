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



standalone = False


import unittestX as unittest
import journal


componentname = 'TOF_monitor2'
category = 'monitors'

class TestCase(unittest.TestCase):

    def test(self):
        "wrap TOF_monitor2"
        
        from mcstas2 import componentfactory
        factory = componentfactory( category, componentname )
        
        component = factory(
            'component',
            nchan=100,
            xmin=-0.1, xmax=0.1, ymin=-0.1, ymax=0.1,
            tmin=0.0, tmax=0.0006,
            filename="tof.dat",
            )
        from mcni.SimulationContext import SimulationContext
        component.simulation_context = SimulationContext()
        component.simulation_context.overwrite_datafiles = True
        component.simulation_context.outputdir = "out-TOF_monitor2"
        
        import mcni
        neutrons = mcni.neutron_buffer( 5 )
        for i in range(5):
            neutrons[i] = mcni.neutron(r=(0,0,-1), v=(0,0,3000), time = 0, prob = 1)
            continue
        component.simulation_context.iteration_no = 0
        component.process( neutrons )
        print(neutrons)
        return

    pass  # end of TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
