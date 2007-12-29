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


class ScattererComputingEngineFactory(object):

    def __init__(self, binding, orientationconvention):
        self.binding = binding
        self.orientationconvention = orientationconvention
        return

    def composite(self, shape, elements, geometer):
        return self.binding.composite( shape, elements, geometer )


    def scatterercontainer(self):
        return self.binding.scatterercontainer( )


    def geometer(self):
        return self.binding.geometer( )


    def position(self, position):
        'convert position (3-tuple) to an object understandable by engine factories'
        return self.binding.position( position )


    def orientation(self, orientation):
        'convert orientation (3-tuple) to an object understandable by engine factories'
        rotmat = self.orientationconvention.angles2matrix( orientation )
        return self.binding.orientation( rotmat )


    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except:
            return getattr(self.binding, name)    

    pass # end of ScattererComputingEngineFactory


# version
__id__ = "$Id$"

# End of file 
