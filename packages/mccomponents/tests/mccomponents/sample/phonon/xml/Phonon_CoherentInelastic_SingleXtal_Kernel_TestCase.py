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
long_test = True


import mcvine
import mccomponents.sample.phonon.xml


sampleassembly_xml = 'sampleassemblies/coh-inel-singlextal/sampleassembly.xml'


import unittestX as unittest
class TestCase(unittest.TestCase):

    def test1(self):
        'coherent inelastic phonon scattering kernel for single crystal'
        from SSD import App
        app = App("test-phonon_coherentinelastic_singlextal_kernel")
        app.run()
        return

    pass  # end of TestCase


if __name__ == "__main__": unittest.main()

# End of file 
