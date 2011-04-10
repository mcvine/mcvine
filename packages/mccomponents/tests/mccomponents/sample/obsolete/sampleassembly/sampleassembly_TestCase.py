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

debug = journal.debug( "sampleassembly_TestCase" )
warning = journal.warning( "sampleassembly_TestCase" )


sampleassembly_xml = 'Ni.xml'


import mcni

class sampleassembly_TestCase(unittest.TestCase):


    def test0(self):
        from sampleassembly.saxml import parse_file
        sa = parse_file( sampleassembly_xml )

        from mccomponents.sample.sampleassembly_support \
             import sampleassembly2compositescatterer, \
             findkernelsfromxmls

        scatterercomposite = findkernelsfromxmls(
            sampleassembly2compositescatterer( sa ) )

        import mccomponents.homogeneous_scatterer as hs
        engine = hs.scattererEngine( scatterercomposite )

        for i in range(10):
            ev = mcni.neutron( r = (0,0,-5), v = (0,0,3000) )
            engine.scatter( ev )
            print ev
            continue
        return
    

    pass  # end of sampleassembly_TestCase


def isKernel(candidate):
    from mccomponents.homogeneous_scatterer.Kernel import Kernel
    return isinstance(candidate, Kernel)


def pysuite():
    suite1 = unittest.makeSuite(sampleassembly_TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
