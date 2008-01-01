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

debug = journal.debug( "mccomposite_TestCase" )
warning = journal.warning( "mccomposite_TestCase" )


import mccomposite, mcni

class mccomposite_TestCase(unittest.TestCase):

    def test(self):
        # create a weird shape
        from mccomposite.geometry import primitives
        block = primitives.block( (1,1,1) )
        sphere = primitives.sphere( 1 )
        cylinder = primitives.cylinder( 2,2.001 )

        from mccomposite.geometry import operations
        dilated = operations.dilate( sphere, 2 )
        translated = operations.translate( block, (0,0,0.5) )
        united = operations.unite( dilated, translated )

        rotated = operations.rotate( united, (90,0,0) )

        intersect = operations.intersect( rotated, cylinder )

        difference = operations.subtract( intersect, sphere )
        
        print mccomposite.scattererEngine( difference )

        shape = difference
        #shape = block
        #shape = dilated
        #shape = united
        #shape = intersect
        #shape = operations.rotate(block, (90,0,0) )
        #shape = rotated
        #shape = sphere
        #shape = operations.subtract(sphere, block)
        #shape = operations.subtract( primitives.cylinder(1, 2.1), sphere )

        #register new scatterer type
        # 1. the pure python class
        from mccomposite.Scatterer import Scatterer
        class NeutronPrinter(Scatterer):
            def identify(self, visitor): return visitor.onNeutronPrinter(self)
            pass
        # 2. the handler to construct c++ engine
        def onNeutronPrinter(self, printer):
            shape = printer.shape()
            cshape = shape.identify(self)
            return self.factory.neutronprinter( cshape )
        # 3. the handler to call python bindings 
        def neutronprinter(self, cshape):
            from neutron_printer2 import cScatterer
            return cScatterer( cshape )
        # 4. register the new class and handlers
        mccomposite.register( NeutronPrinter, onNeutronPrinter,
                             {'BoostPythonBinding':neutronprinter} )

        #create pure python representation of scatterer composite
        composite = mccomposite.composite( shape )
        nprinter = NeutronPrinter( shape )
        composite.addElement( nprinter )

        #render the c++ representation
        ccomposite = mccomposite.scattererEngine( composite )

        ev = mcni.neutron( r = (0,0,-5), v = (0,0,1) )
        ccomposite.scatter(ev)
        
        return


    pass  # end of mccomposite_TestCase



def pysuite():
    suite1 = unittest.makeSuite(mccomposite_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    #journal.debug("mccomposite.geometry.ArrowIntersector").activate()
    #journal.debug("mccomposite.geometry.Locator").activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
