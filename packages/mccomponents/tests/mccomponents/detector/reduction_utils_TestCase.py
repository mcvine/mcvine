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


import unittestX as unittest, os

class TestCase(unittest.TestCase):

    def test1(self):
        try:
            from mccomponents.detector.reduction_utils import events2IQE
            eventsfile = 'events.dat'
            outfile = 'intensities.dat'
            nevents = 337
            arcs_res = os.path.join(
                mcvine_resources, 'instruments/ARCS/reduction',)
            pixelpositionsfile = os.path.join(
                arcs_res, 'pixelID2position.bin')
            solidanglesfile = os.path.join(
                arcs_res, 'solidangles.bin')
            npixels = 117760
            import pyre.units.length
            import pyre.units.energy
            import pyre.units.time
            iqe = events2IQE(
                eventsfile, nevents, 
                outfile,
                pixelpositionsfile, 
                solidanglesfile,
                npixels,
                mod2sample=13.6*pyre.units.length.meter,
                Ei=700*pyre.units.energy.meV,
                Qaxis=(9.5,10.5,0.02), Eaxis=(30,120,1.),
                tofUnit=1*pyre.units.time.microsecond,
                toffset=0*pyre.units.time.s,
                tofmax=0.015*pyre.units.time.s,
                )
            global interactive
            if interactive:
                from histogram.plotter import defaultPlotter
                defaultPlotter.plot(iqe)
        except:
            print("Deprecated functionality has beed removed")
        return

    pass  # end of detector_TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    import journal
    journal.debug("Event2QE").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    

interactive = False    
if __name__ == "__main__":
    interactive = True
    main()

    
# version
__id__ = "$Id: detector_simple_TestCase.py 855 2011-02-09 16:41:24Z linjiao $"

# End of file 
