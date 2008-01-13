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

debug = journal.debug( "kernelxml_TestCase" )
warning = journal.warning( "kernelxml_TestCase" )


datapath = 'SQE-examples'
kernelxml = 'Ni-scatteringkernel.xml'


class kernelxml_TestCase(unittest.TestCase):


    def test0(self):
        from mccomposite.geometry import primitives
        shape = primitives.block( (1,1,1) )
        
        from mccomponents.homogeneous_scatterer import homogeneousScatterer
        scatterer = homogeneousScatterer( shape, None )
        
        from mccomponents.sample.kernelxml import parse_file
        kernel = parse_file( kernelxml, scatterer )

        self.assert_( isKernel( kernel ) )
        self.assertEqual( scatterer.kernel(), kernel )
        return
    

    pass  # end of kernelxml_TestCase


def isKernel(candidate):
    from mccomponents.homogeneous_scatterer.Kernel import Kernel
    return isinstance(candidate, Kernel)


def pysuite():
    suite1 = unittest.makeSuite(kernelxml_TestCase)
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
