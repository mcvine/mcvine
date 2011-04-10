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

    def test2(self):
        'coherent inelastic phonon scattering kernel for single crystal'
        from SSD import App
        app = App("test-phonon_coherentinelastic_singlextal_kernel")
        app.run()
        return
    
    pass  # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug('phonon_coherent_inelastic_polyxtal_kernel').activate()
    #journal.debug('random').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
