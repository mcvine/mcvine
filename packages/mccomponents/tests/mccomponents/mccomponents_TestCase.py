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


import mccomponents, mccomposite, mcni

# python class from new kernel
from mccomponents.homogeneous_scatterer.Kernel import Kernel
class NeutronPrinter(Kernel):
    def identify(self, visitor): return visitor.onNeutronPrinter(self)
    pass

#register new kernel type
# 2. the handler to construct c++ engine
def onNeutronPrinter(self, printer):
    return self.factory.neutronprinter( )
# 3. the handler to call python bindings 
def neutronprinter(self):
    from neutron_printer3 import cKernel
    return cKernel( )
# 4. register the new class and handlers
mccomponents.homogeneous_scatterer.register (
    NeutronPrinter, onNeutronPrinter,
    {'BoostPythonBinding':neutronprinter} )

class mccomponents_TestCase(unittest.TestCase):

    def __init__(self, *args, **kwds):
        unittest.TestCase.__init__(self, *args, **kwds)
        return
        

    def test(self):
        '''create pure python representation of a composite kernel,
        and render the c++ computation engine of that kernel
        '''
        #create pure python representation of kernel composite
        composite_kernel = mccomponents.homogeneous_scatterer.compositeKernel()
        nprinter = NeutronPrinter( )
        composite_kernel.addElement( nprinter )

        #render the c++ representation
        ccomposite_kernel = mccomponents.homogeneous_scatterer.kernelEngine(
            composite_kernel )

        ev = mcni.neutron( r = (0,0,0), v = (0,0,1) )
        ccomposite_kernel.scatter(ev)

        return


    def test2(self):
        '''create pure python representation of a homogeneous scatterer,
        and render the c++ computation engine of that kernel
        '''
        from mccomposite.geometry import primitives
        shape = primitives.block( (1,1,1) )
        nprinter = NeutronPrinter( )
        scatterer = mccomponents.homogeneous_scatterer.homogeneousScatterer(shape, nprinter)

        #render the c++ representation
        cscatterer = mccomponents.homogeneous_scatterer.scattererEngine( scatterer )

        for i in range(10):
            ev = mcni.neutron( r = (0,0,-5), v = (0,0,1) )
            cscatterer.scatter(ev)
            continue
        return
    

    def test3(self):
        '''create pure python representation of a homogeneous scatterer with
        composite kernel. render the c++ computation engine of that kernel.
        '''
        #shape
        from mccomposite.geometry import primitives
        shape = primitives.block( (1,1,1) )

        #kernel
        nprinter = NeutronPrinter( )
        
        #composite kernel
        composite_kernel = mccomponents.homogeneous_scatterer.compositeKernel()
        composite_kernel.addElement( nprinter )

        #scatterer
        scatterer = mccomponents.homogeneous_scatterer.homogeneousScatterer(
            shape, composite_kernel)

        #render the c++ representation
        cscatterer = mccomponents.homogeneous_scatterer.scattererEngine( scatterer )

        for i in range(10):
            ev = mcni.neutron( r = (0,0,-5), v = (0,0,1) )
            cscatterer.scatter(ev)
            continue
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
