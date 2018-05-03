#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'


import unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'mcni: instrument and simulate'
        import mcni, mcstas2
        i = mcni.instrument() # created an instrument
        g = mcni.geometer()   # created a geometer
        f = mcni.componentfactory('sources', 'Source_simple', 'mcstas2') # get a component factory
        # help(f)
        # add source
        s = f('source')  # instantiate a Source_simple component
        i.append(s) # add the component to the instrument
        g.register(s, (0,0,0), (0,0,0))  # register the new component with the geometer
        # add monitor
        f = mcni.componentfactory('monitors', 'E_monitor', 'mcstas2')
        m = f('monitor', filename="mon.dat")
        i.append(m) # add the component to the instrument
        g.register(m, (0,0,1), (0,0,0))  # register the new component with the geometer
        #
        neutrons = mcni.neutron_buffer(5) # created a neutron buffer of size 5
        print neutrons  
        mcni.simulate(i, g, neutrons, outputdir='out-instrument0', iteration_no=0, overwrite_datafiles=True)  # run the simulation
        print neutrons
        return

    pass  # end of TestCase



if __name__ == "__main__": unittest.main()
    
# End of file 
