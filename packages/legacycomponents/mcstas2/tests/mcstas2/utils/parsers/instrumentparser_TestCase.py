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


from mcvine.deployment_info import mcvine_resources
if not mcvine_resources:
    skip = True


import unittestX as unittest
import journal, os


class TestCase(unittest.TestCase):

    def test(self):
        from mcstas2.utils.parsers.McStasInstrumentParser import McStasInstrumentParser
        parser = McStasInstrumentParser()
        path = os.path.join(
            mcvine_resources, 
            "instruments/VULCAN/resources/vulcan_asbuilt_L2d.instr"
            )
        text = open(path).read()
        instrument = parser.parse(text)
        return

    pass  # end of TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
