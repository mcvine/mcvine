#!/usr/bin/env python
#
#

standalone = True
interactive = False


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


    def test2(self):
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
        from mcni.utils import conversion as muc
        import numpy as np
        Es = []; ps = []
        for Ei in np.arange(5., 50., 0.1):
            vi = 0,0,muc.e2v(Ei)
            for i in range(100):
                ev = mcni.neutron( r = (0,0,-5), v = vi )
                engine.scatter( ev )
                p = ev.probability
                if p<0: continue
                v = np.array(ev.state.velocity)
                v = np.linalg.norm(v)
                Ef = muc.v2e(v)
                E = Ei - Ef
                Es.append(E)
                ps.append(p)
            continue
        I, Ebb = np.histogram(Es, bins=100, weights=ps)
        Ec = (Ebb[1:] + Ebb[:-1])/2.
        global interactive
        if interactive:
            import matplotlib as mpl
            mpl.use('Agg')
            from matplotlib import pyplot as plt
            plt.plot(Ec, I)
            plt.savefig('_fig_test2_Phonon_IncoherentInelastic_EnergyFocusing_Kernel.png')
        return


    pass  # end of TestCase


def isKernel(candidate):
    from mccomponents.homogeneous_scatterer.Kernel import Kernel
    return isinstance(candidate, Kernel)


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    global interactive
    interactive = True
    #debug.activate()
    journal.debug('phonon_incoherent_inelastic_kernel').activate()
    #journal.debug('random').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":    main()
    
# End of file 
