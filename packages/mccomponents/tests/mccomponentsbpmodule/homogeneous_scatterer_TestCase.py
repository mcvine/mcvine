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


import mcni
from mcni import mcnibp
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

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
        
        weights = mccomponentsbp.vector_double(0)
        weights.append(1.)

        rotmats = mccomponentsbp.vector_rotmat(0)
        rotmat = mcnibp.RotationMatrix_double(1,0,0, 0,1,0, 0,0,1)
        rotmats.append(rotmat)
        
        average=False
        kernelcomposite = mccomponentsbp.CompositeScatteringKernel( 
            kernels, weights, rotmats, average)

        mcweights = mccomponentsbp.MCWeights_AbsorptionScatteringTransmission()
        scatterer = mccomponentsbp.HomogeneousNeutronScatterer(
            shape, kernelcomposite, mcweights )

        for i in range(10):
            ev = mcni.neutron( r = (0,0,-5), v = (0,0,1) )
            scatterer.scatter(ev)
            continue
        return


    def testRandom(self):
        'random, srandom'
        binding = mccomponentsbp
        
        binding.srandom( 1 )
        r11 = binding.random( 0, 1 )
        r12 = binding.random( 0, 1 )
        self.assertTrue( r11 != r12 )
        self.assertTrue( r11 >=0 and r11 <=1 )
        self.assertTrue( r12 >=0 and r12 <=1 )

        binding.srandom( 2 )
        r21 = binding.random( 0, 1 )
        r22 = binding.random( 0, 1 )
        self.assertTrue( r21 != r22 )
        self.assertTrue( r21 >=0 and r21 <=1 )
        self.assertTrue( r22 >=0 and r22 <=1 )
        self.assertTrue( r21 != r11 )
        self.assertTrue( r22 != r12 )
        
        binding.srandom( 1 )
        r31 = binding.random( 0, 1 )
        r32 = binding.random( 0, 1 )
        self.assertTrue( r31 != r32 )
        self.assertTrue( r31 >=0 and r31 <=1 )
        self.assertTrue( r32 >=0 and r32 <=1 )
        self.assertTrue( r31 == r11 )
        self.assertTrue( r32 == r12 )
        return

    pass  # end of TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    unittest.main()
    # main()
    
# version
__id__ = "$Id$"

# End of file 
