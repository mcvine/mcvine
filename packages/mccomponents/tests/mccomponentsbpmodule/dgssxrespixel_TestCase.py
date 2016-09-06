#!/usr/bin/env python
#



import unittestX as unittest
import journal

debug = journal.debug( "homogeneous_scatterer_TestCase" )
warning = journal.warning( "homogeneous_scatterer_TestCase" )


import mcni
from mcni import mcnibp
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def testHomogeneousNeutronScatterer(self):
        'HomogeneousNeutronScatterer'
        shape = mccompositebp.Cylinder(0.025/2., 0.01)
        tof=0.001; pressure=10*101325
        pixel = mccomponentsbp.DGSSXResPixel(tof, pressure, shape)
        
        ev = mcni.neutron( r = (0,0,-3), v = (0,0,3000) )
        pixel.scatter(ev)
        print ev.probability
        return

    pass  # end of TestCase

    
if __name__ == "__main__": unittest.main()
    
# End of file 
