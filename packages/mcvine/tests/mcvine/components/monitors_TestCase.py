#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'


import unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'mcvine: simulate'
        # this is the example 1 in the mcvine package documentation
        import mcvine, mcvine.components
        i = mcvine.instrument()
        # add source
        i.append(mcvine.components.sources.Source_simple('source'), position=(0,0,0))
        # add monitor
        i.append(mcvine.components.monitors.L_monitor('monitor', filename='IL.dat'), position=(0,0,1))
        #
        try:
            neutrons = i.simulate(5,outputdir="out-mcvine", overwrite_datafiles=True, iteration_no=0)
        except Exception as e:
            assert "bad detector dimension" in str(e)
            return
        raise RuntimeError("Expecting an exception")
        return

    def test1a(self):
        import mcvine, mcvine.components
        i = mcvine.instrument()
        # add source
        i.append(mcvine.components.sources.Source_simple('source'), position=(0,0,0))
        # add monitor
        m = mcvine.components.monitors.L_monitor(
            'monitor', Lmin=0, Lmax=15, nchan=150, xwidth=.01, yheight=.01, filename='IL.data')
        i.append(m, position=(0,0,1))
        neutrons = i.simulate(5,outputdir="out-mcvine", overwrite_datafiles=True, iteration_no=0)
        return

    
    def test2(self):
        'mcvine: simulate'
        # this is the example 1 in the mcvine package documentation
        import mcvine, mcvine.components
        i = mcvine.instrument()
        # add source
        i.append(mcvine.components.sources.Source_simple('source'), position=(0,0,0))
        # add monitor
        i.append(mcvine.components.monitors.PSD_monitor('monitor'), position=(0,0,1))
        #
        try:
            neutrons = i.simulate(5,outputdir="out-mcvine", overwrite_datafiles=True, iteration_no=0)
        except Exception as e:
            assert "bad detector dimension" in str(e)
            return
        raise RuntimeError("Expecting an exception")
        return


    pass  # end of TestCase



if __name__ == "__main__": unittest.main(); print(1)
    
# End of file 
