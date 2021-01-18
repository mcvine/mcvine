#!/usr/bin/env python
#
#


standalone = True
long_test = True


import mcvine
import mccomponents.sample.phonon.xml


sampleassembly_xml = 'sampleassemblies/coh-inel-singlextal/sampleassembly.xml'


import unittestX as unittest
class TestCase(unittest.TestCase):

    def test2(self):
        'coherent inelastic phonon scattering kernel for single crystal. Ei small compare to dispersions'
        from SSD import App
        app = App("test-phonon_coherentinelastic_singlextal_kernel-2")
        app.run()
        return
    pass  # end of TestCase


if __name__ == "__main__": unittest.main()

# End of file 
