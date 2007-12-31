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

debug = journal.debug( "mccomponents_TestCase" )
warning = journal.warning( "mccomponents_TestCase" )


import mccomponents, mcni

class mccomponents_TestCase(unittest.TestCase):

    def test(self):
        '''create pure python representation of a composite kernel,
        and render the c++ computation engine of that kernel
        '''
        #register new kernel type
        # 1. the pure python class
        from mccomponents.Kernel import Kernel
        class NeutronPrinter(Kernel):
            def identify(self, visitor): return visitor.onNeutronPrinter(self)
            pass
        # 2. the handler to construct c++ engine
        def onNeutronPrinter(self, printer):
            return self.factory.neutronprinter( )
        # 3. the handler to call python bindings 
        def neutronprinter(self):
            from neutron_printer3 import cKernel
            return cKernel( )
        # 4. register the new class and handlers
        mccomponents.register( NeutronPrinter, onNeutronPrinter,
                             {'BoostPythonBinding':neutronprinter} )

        #create pure python representation of kernel composite
        composite_kernel = mccomponents.compositeKernel()
        nprinter = NeutronPrinter( )
        composite_kernel.addElement( nprinter )

        #render the c++ representation
        ccomposite_kernel = mccomponents.kernelEngine( composite_kernel )

        ev = mcni.neutron( r = (0,0,0), v = (0,0,1) )
        ccomposite_kernel.scatter(ev)
        
        return
            
    pass  # end of mccomponents_TestCase



def pysuite():
    suite1 = unittest.makeSuite(mccomponents_TestCase)
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
