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

debug = journal.debug( "scattererxml_TestCase" )
warning = journal.warning( "scattererxml_TestCase" )


scattererxml = 'Ni-scatterer.xml'


class scattererxml_TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.kernelxml.parser'
        from mccomponents.sample.kernelxml import parse_file
        scatterer = parse_file( scattererxml )

        kernel = scatterer.kernel()
        self.assert_( isKernel( kernel ) )
        return
    

    def test2(self):
        'mccomponents.sample.kernelxml.renderer'
        from mccomponents.sample.kernelxml import parse_file, render
        scatterer = parse_file( scattererxml )
        
        renderedxml = "%s.rendered" % scattererxml
        print >>open(renderedxml,'w'), '\n'.join(render(scatterer))

        scatterer1 = parse_file( renderedxml )
        return
    

    pass  # end of scattererxml_TestCase


def isKernel(candidate):
    from mccomponents.homogeneous_scatterer.Kernel import Kernel
    return isinstance(candidate, Kernel)


def pysuite():
    suite1 = unittest.makeSuite(scattererxml_TestCase)
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
