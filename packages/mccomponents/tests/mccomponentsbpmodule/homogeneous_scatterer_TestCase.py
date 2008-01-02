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

debug = journal.debug( "homogeneous_scatterer_TestCase" )
warning = journal.warning( "homogeneous_scatterer_TestCase" )


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class homogeneous_scatterer_TestCase(unittest.TestCase):

    def testHomogeneousNeutronScatterer(self):
        'HomogeneousNeutronScatterer'
        shape = mccompositebp.Block(1,1,1)

        from neutron_printer3 import cKernel as Printer
        printer = Printer( )

        mcweights = mccomponentsbp.MCWeights_AbsorptionScatteringTransmission()
        scatterer = mccomponentsbp.HomogeneousNeutronScatterer(
            shape, printer, mcweights )

        for i in range(10):
            ev = mcni.neutron( r = (0,0,-5), v = (0,0,1) )
            scatterer.scatter(ev)
            continue
        return

    def testCompositeScatteringKernel(self):
        'CompositeScatteringKernel'
        shape = mccompositebp.Block(1,1,1)

        from neutron_printer3 import cKernel as Printer
        printer = Printer( )

        kernels = mccomponentsbp.pointer_vector_Kernel(0)
        kernels.append( printer )

        kernelcomposite = mccomponentsbp.CompositeScatteringKernel( kernels )

        mcweights = mccomponentsbp.MCWeights_AbsorptionScatteringTransmission()
        scatterer = mccomponentsbp.HomogeneousNeutronScatterer(
            shape, kernelcomposite, mcweights )

        for i in range(10):
            ev = mcni.neutron( r = (0,0,-5), v = (0,0,1) )
            scatterer.scatter(ev)
            continue
        return

    pass  # end of homogeneous_scatterer_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(homogeneous_scatterer_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
