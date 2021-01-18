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


import unittestX as unittest
import journal

debug = journal.debug( "IsotropicKernel_TestCase" )
warning = journal.warning( "IsotropicKernel_TestCase" )


import mcni, mccomposite, mccomponents.sample as ms, mccomponents.homogeneous_scatterer as mh

class IsotropicKernel_TestCase(unittest.TestCase):

    def test1(self):
        'IsotropicKernel'
        kernel = ms.isotropickernel( 1., 1. )
        
        ckernel = mh.scattererEngine( kernel )
        
        ev = mcni.neutron( r = (-5,0,0), v = (3000,0,0) )
        
        ckernel.scatter(ev)
        print(ev)
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
