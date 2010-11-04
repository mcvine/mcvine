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



import mcvine
import unittestX as unittest
import journal

debug = journal.debug( "mcni.pyre_support.test" )
warning = journal.warning( "mcni.pyre_support.test" )



class TestCase(unittest.TestCase):


    def test1(self):
        'mcni.pyre_support: componentfactory'
        from mcni.pyre_support import componentfactory
        f = componentfactory( 'sources', 'MonochromaticSource' )
        from mcni.pyre_components.MonochromaticSource import MonochromaticSource
        self.assertEqual( f, MonochromaticSource )

        f1 = componentfactory( 'sources', 'Source_simple', 'mcstas2' )
        import mcstas2.pyre_support 
        f1a = mcstas2.pyre_support.componentfactory( 'sources', 'Source_simple' )
        self.assertEqual( f1, f1a )
        return


    def test2(self):
        'mcni.pyre_support: findcomponentfactory'
        from mcni.pyre_support import findcomponentfactory
        f = findcomponentfactory('MonochromaticSource' )
        from mcni.pyre_components.MonochromaticSource import MonochromaticSource
        self.assertEqual( f, MonochromaticSource )

        f1 = findcomponentfactory('Source_simple')
        import mcstas2.pyre_support 
        f1a = mcstas2.pyre_support.componentfactory( 'sources', 'Source_simple' )
        self.assertEqual( f1, f1a )
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
    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
