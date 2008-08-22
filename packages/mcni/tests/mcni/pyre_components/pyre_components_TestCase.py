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

debug = journal.debug( "mcni.pyre_components.test" )
warning = journal.warning( "mcni.pyre_components.test" )



class TestCase(unittest.TestCase):

    def test1(self):
        from mcni.pyre_components import componentfactory
        f = componentfactory( 'sources', 'MonochromaticSource' )
        from mcni.pyre_components.MonochromaticSource import MonochromaticSource
        self.assertEqual( f, MonochromaticSource )
        return

    def test2(self):
        from mcni.pyre_components import componentfactory
        f = componentfactory( 'monitors', 'NeutronPrinter' )
        from mcni.pyre_components.NeutronPrinter import NeutronPrinter
        self.assertEqual( f, NeutronPrinter )
        return

    pass # end of TestCase


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
