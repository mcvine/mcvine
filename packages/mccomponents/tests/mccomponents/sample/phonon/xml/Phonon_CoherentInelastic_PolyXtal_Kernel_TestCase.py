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

#debug = journal.debug( "TestCase" )
#warning = journal.warning( "TestCase" )


#
import mccomponents.sample.phonon.xml
import mcni


scattererxml = 'fccNi-plate-scatterer.xml'
sampleassembly_xml = 'fccNi-plate-sampleassembly.xml'

class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.kernelxml.parser'
        from mccomponents.sample.kernelxml import parse_file
        scatterer = parse_file( scattererxml )

        kernel = scatterer.kernel()
        print kernel
        self.assert_( isKernel( kernel ) )
        
        return


    def test1a(self):
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


    def test2(self):
        'instrument: monochromatic source, sample, S(Q,E) detector'
        mod2sample = 10. # meter
        Ei = 70
        from mcni.utils import e2v
        vi = e2v( Ei ) #m/s

        Emin = -60; Emax = 60; nE = 120
        Qmin = 0; Qmax = 11; nQ = 110

        from SSD import Instrument as base
        class Instrument(base):

            class Inventory(base.Inventory):

                from mcni.pyre_support import facility, componentfactory as component
                detector = facility(
                    'detector',
                    default = component( 'monitors', 'IQE_monitor', supplier = 'mcstas2')\
                    ('detector') )
                
                pass # end of Inventory
            
            def __init__(self, name = "test-phonon_coherentinelastic_polyxtal_kernel"):
                base.__init__(self, name)
                return
            
            def _defaults(self):
                base._defaults(self)
                
                geometer = self.inventory.geometer
                geometer.inventory.source = (0,0,0), (0,0,0)
                geometer.inventory.sample = (0,0,mod2sample), (0,0,0)
                geometer.inventory.detector = (0,0,mod2sample), (0,0,0)

                source = self.inventory.source
                source.inventory.position = 0,0,0
                source.inventory.velocity = 0,0,vi
                source.inventory.probability = 1
                source.inventory.time = 0.0

                sample = self.inventory.sample
                sample.inventory.xml = sampleassembly_xml

                detector = self.inventory.detector
                detector.inventory.Ei = Ei
                detector.inventory.Qmin = Qmin
                detector.inventory.Qmax = Qmax
                detector.inventory.nQ = nQ
                detector.inventory.Emin = Emin
                detector.inventory.Emax = Emax
                detector.inventory.nE = nE
                return

            def _init(self):
                base._init(self)
                detector = self.inventory.detector
                from mcstas2.pyre_support.monitor_exts import extend
                extend( detector )
                return
            
            pass # end of Instrument

        app = Instrument()
        app.run()
        return
    

    def g_test2(self):
        'mccomponents.sample.kernelxml.renderer'
        from mccomponents.sample.kernelxml import parse_file, render
        scatterer = parse_file( scattererxml )
        
        renderedxml = "%s.rendered" % scattererxml
        print >>open(renderedxml,'w'), '\n'.join(render(scatterer))

        scatterer1 = parse_file( renderedxml )
        return
    

    pass  # end of TestCase


def isKernel(candidate):
    from mccomponents.homogeneous_scatterer.Kernel import Kernel
    return isinstance(candidate, Kernel)


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug('phonon_coherent_inelastic_polyxtal_kernel').activate()
    #journal.debug('random').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
