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



standalone = True


import unittestX as unittest
import journal

#debug = journal.debug( "TestCase" )
#warning = journal.warning( "TestCase" )


#
import mcvine
import mccomponents.sample.phonon.xml
import mcni


scattererxml = 'sampleassemblies/coh-inel-polyxtal/fccNi-plate-scatterer.xml'
sampleassembly_xml = 'sampleassemblies/coh-inel-polyxtal/sampleassembly.xml'

class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.kernelxml.parser'
        from mccomponents.sample.kernelxml import parse_file
        import os
        dir, filename = os.path.split(scattererxml)
        save = os.path.abspath(os.curdir)
        os.chdir(dir)
        scatterer = parse_file( filename )
        os.chdir(save)

        kernel = scatterer.kernel()
        print kernel
        self.assert_( isKernel( kernel ) )
        
        return


    def test1a(self):
        from sampleassembly.saxml import parse_file
        import os
        dir, filename = os.path.split(sampleassembly_xml)
        save = os.path.abspath(os.curdir)
        os.chdir(dir)
        sa = parse_file( filename )

        from mccomponents.sample.sampleassembly_support \
             import sampleassembly2compositescatterer, \
             findkernelsfromxmls

        scatterercomposite = findkernelsfromxmls(
            sampleassembly2compositescatterer( sa ) )

        import mccomponents.homogeneous_scatterer as hs
        engine = hs.scattererEngine( scatterercomposite )

        os.chdir(save)
        for i in range(10):
            ev = mcni.neutron( r = (0,0,-5), v = (0,0,3000) )
            engine.scatter( ev )
            print ev
            continue

        return


    def test2(self):
        'instrument: monochromatic source, sample, S(Q,E) detector'
        from SSD import App
        app = App("test-phonon_coherentinelastic_polyxtal_kernel")
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
