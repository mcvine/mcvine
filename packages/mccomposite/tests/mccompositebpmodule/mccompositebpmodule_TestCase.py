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

debug = journal.debug( "mccompositebpmodule_TestCase" )
warning = journal.warning( "mccompositebpmodule_TestCase" )


import mcni
from mccomposite import mccompositebp as binding

class mccompositebpmodule_TestCase(unittest.TestCase):

    def testGeometer(self):
        'geometer'
        geometer = binding.Geometer_NeutronScatterer( );
        return


    def testCompositeNeutronScatterer(self):
        'CompositeNeutronScatterer'
        geometer = binding.Geometer_NeutronScatterer( );
        shape = binding.Block(1,1,1)

        from neutron_printer2 import cScatterer as Printer
        printer = Printer( shape )

        scatterers = binding.pointer_vector_NeutronScatterer(0)
        scatterers.append( printer )

        cs = binding.CompositeNeutronScatterer( shape, scatterers, geometer )

        ev = mcni.neutron( r = (0,0,-5), v = (0,0,1) )

        cs.scatter(ev)
        return

    pass  # end of mccompositebpmodule_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(mccompositebpmodule_TestCase)
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
