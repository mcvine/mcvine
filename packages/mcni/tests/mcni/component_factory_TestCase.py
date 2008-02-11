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

debug = journal.debug( "mcni_component_factory_TestCase" )
warning = journal.warning( "mcni_component_factory_TestCase" )


import mcni

class TestCase(unittest.TestCase):


    def test(self):
        'mcni: component factory'
        from mcni import componentfactory, componentinfo
        print 'mcni, sources, MonochromaticSource',  componentfactory( 'sources', 'MonochromaticSource'), componentinfo( 'sources', 'MonochromaticSource' )
        print 'mcni, sources, MonochromaticSource',  componentfactory( 'sources', 'MonochromaticSource', 'mcni'), componentinfo( 'sources', 'MonochromaticSource', 'mcni' )
        print 'mcstas2, sources, Source_simple',  componentfactory( 'sources', 'Source_simple', 'mcstas2'), componentinfo( 'sources', 'Source_simple', 'mcstas2' )
        return
    
        
    pass  # end of TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
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
