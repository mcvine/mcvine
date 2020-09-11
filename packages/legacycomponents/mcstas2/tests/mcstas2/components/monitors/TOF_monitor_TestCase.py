#!/usr/bin/env python
#
#


import unittestX as unittest

componentname = 'TOF_monitor'
category = 'monitors'

class TestCase(unittest.TestCase):

    def test(self):
        "wrap TOF_monitor2"
        
        from mcstas2 import componentfactory
        factory = componentfactory( category, componentname )
        
        component = factory('component', filename="tof.dat", xwidth=0.1, yheight=0.1)
        from mcni.SimulationContext import SimulationContext
        component.simulation_context = SimulationContext()
        component.simulation_context.overwrite_datafiles = True
        component.simulation_context.outputdir = "out-TOF_monitor"
        
        import mcni
        neutrons = mcni.neutron_buffer( 5 )
        for i in range(5):
            neutrons[i] = mcni.neutron(r=(0,0,-1), v=(0,0,3000), time = 0, prob = 1)
            continue
        component.simulation_context.iteration_no = 0
        component.process( neutrons )
        component._saveFinalResult()
        print(neutrons)
        return

    pass  # end of TestCase


if __name__ == "__main__": unittest.main()
    
# End of file 
