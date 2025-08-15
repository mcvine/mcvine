#!/usr/bin/env python
#
#
standalone = True

import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'

import unittest

import mcvine
import mccomponents.sample.phonon.xml
import mcni

scattererxml = 'sampleassemblies/sans_spheres/sans_spheres-scatterer.xml'
sampleassembly_xml = 'sampleassemblies/sans_spheres/sampleassembly.xml'

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
        print(kernel)
        self.assertTrue( isKernel( kernel ) )
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
        for i in range(1000):
            ev = mcni.neutron( r = (0,0,-5), v = (0,0,3000) )
            engine.scatter( ev )
            # print ev
            continue
        return

    pass  # end of TestCase

def isKernel(candidate):
    from mccomponents.homogeneous_scatterer.Kernel import Kernel
    return isinstance(candidate, Kernel)

def main(): unittest.main()
if __name__ == "__main__": main()

# End of file
