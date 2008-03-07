#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from mccomponents.homogeneous_scatterer.Kernel import Kernel

class He3TubeKernel(Kernel):

    def __init__(self, pressure, tubeIndexes, 
                 tubeLength, npixels, axisDirection, pixel0position):
        '''new He3 detector tube kernel
        pressure: gas pressure of He3. with units
        tubeIndexes: indexes to identify the tube
        '''
        self.pressure = pressure
        self.tubeIndexes = tubeIndexes
        self.tubeLength = tubeLength
        self.npixels = npixels
        self.axisDirection = axisDirection
        self.pixel0position = pixel0position
        return
        
    def identify(self, visitor): return visitor.onHe3TubeKernel(self)
    
    pass


# version
__id__ = "$Id$"

# End of file 
