#!/usr/bin/env python
#
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


scattererxml = 'sampleassemblies/incoh-inel-energy-focusing/fccNi-plate-scatterer.xml'
sampleassembly_xml = 'sampleassemblies/incoh-inel-energy-focusing/sampleassembly.xml'

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
            ev = mcni.neutron( r = (0,0,-5), v = (0,0,1000) )
            engine.scatter( ev )
            print ev
            continue

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
    journal.debug('phonon_incoherent_inelastic_kernel').activate()
    #journal.debug('random').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":    main()
    
# End of file 
