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
        i = mcni.instrument()
        # add source
        f = mcni.componentfactory('sources', 'Source_simple', 'mcstas2')
        s = f('source')
        i.append(s, position=(0,0,0))
        # add monitor
        f = mcni.componentfactory('monitors', 'E_monitor', 'mcstas2')
        m = f('monitor', filename="mon.dat")
        i.append(m, position=(0,0,1))
        #
        neutrons = i.simulate(5, outputdir="out-instrument", overwrite_datafiles=True, iteration_no=0)
        print(neutrons)
        return

    
    pass  # end of TestCase



if __name__ == "__main__": unittest.main()
    
# End of file 
