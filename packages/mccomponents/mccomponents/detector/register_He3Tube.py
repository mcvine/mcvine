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


import units


# the interface
from mccomposite.CompositeScatterer import CompositeScatterer as base
class He3Tube(base):
    def __init__(self, shape, id = 0, pressure = units.pressure.atm,
                 mcweights_absorption_scattering_transmission = (0.9,0,0.1) ):
        base.__init__(self, shape)
        self._id = id
        self._pressure = pressure
        self.mcweights_absorption_scattering_transmission = mcweights_absorption_scattering_transmission
        return
    def id(self): return self._id
    def pressure(self): return self._pressure
    def identify(self, visitor): return visitor.onHe3Tube(self)
    pass


class Pixel:
    def __init__(self, id = 0):
        self._id = id
        return
    def id(self): return self._id
    pass

    
# 2. the handler to construct c++ engine
def onHe3Tube(self, he3tube):
    from mccomposite.geometry import locate
    
    # assume all elements of he3tube are pixels
    pixels = he3tube.elements()
    npixels = len(pixels) 

    #shape of he3tube
    shape = he3tube.shape()
    if not shape: raise "shape of he3tube %s is not specified" % he3tube
    cshape = shape.identify(self)

    #make sure pixels are in the he3tube
    geometer = he3tube.geometer
    for element in pixels:
        position = geometer.position(element)/units.length.meter
        assert locate( position, shape ) == "inside"
        continue

    #find the axis direction of the he3tube tube
    pixel0position = geometer.position(pixels[0]) / units.length.meter
    axisDirection = geometer.position(pixels[-1]) / units.length.meter - pixel0position
    import numpy, numpy.linalg as nl
    axisDirection = numpy.array(axisDirection)
    len1 = float(nl.norm(axisDirection))
    axisDirection /= len1
    #detector length. len1 is the length of (n-1) pixels
    tubeLength = len1 * npixels / (npixels-1)

    #pressure
    pressure = he3tube.pressure()

    #kernel
    import mccomponents.detector as md
    kernel = md.he3tubeKernel(
        pressure, self._indexes_in_detsys,
        tubeLength, npixels, axisDirection, pixel0position)

    # treat this detector as  a homogeneous scatterer
    import mccomponents.homogeneous_scatterer as mh
    scatterer = mh.homogeneousScatterer(
        shape, kernel,
        mcweights_absorption_scattering_transmission \
        = he3tube.mcweights_absorption_scattering_transmission )
    return scatterer.identify(self)



# 4. register the new class and handlers
import mccomposite
mccomposite.register_engine_ctor (He3Tube, onHe3Tube )



# version
__id__ = "$Id$"

# End of file 
