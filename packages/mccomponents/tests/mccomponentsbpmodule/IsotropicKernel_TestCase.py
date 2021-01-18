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



import unittestX as unittest
import journal

debug = journal.debug( "IsotropicKernel_TestCase" )
warning = journal.warning( "IsotropicKernel_TestCase" )


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class IsotropicKernel_TestCase(unittest.TestCase):

    def test(self):
        kernel = mccomponentsbp.IsotropicKernel(1,1)

        for i in range(10):
            event = mcni.neutron( r = (0,0,0), v = (0,0,3000), prob = 1, time = 0 )
            kernel.scatter( event );
            print(event)
            continue

        return
    
    
    pass  # end of IsotropicKernel_TestCase

    
def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
