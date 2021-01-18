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
        i.append(mcvine.components.monitors.E_monitor('monitor', filename='IE.dat'), position=(0,0,1))
        #
        neutrons = i.simulate(5,outputdir="out-mcvine", overwrite_datafiles=True, iteration_no=0)
        print(neutrons)
        return

    
    def test2(self):
        'mcvine: list component types'
        # this is the example 3 in the mcvine package documentation
        import mcvine
        mcvine.listallcomponentcategories()
        mcvine.listcomponentsincategory('sources')
        return


    def test3(self):
        "mcvine: units"
        from mcvine import units
        self.assertEqual(units.meter, units.m)
        self.assertEqual(units.meter, units.parse('meter'))
        return

    
    pass  # end of TestCase



if __name__ == "__main__": unittest.main()
    
# End of file 
