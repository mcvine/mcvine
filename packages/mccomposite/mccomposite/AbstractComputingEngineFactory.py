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


class AbstractComputingEngineFactory(object):

    '''factory class of computing engine of scatterers
    '''

    def composite(self, shape, elements, geometer):
        raise NotImplementedError


    def scatterercontainer(self):
        raise NotImplementedError


    def geometer(self):
        raise NotImplementedError


    def position(self, position):
        'convert position (3-tuple) to an object understandable by engine factories'
        raise NotImplementedError


    def orientation(self, orientation):
        'convert orientation (3-tuple) to an object understandable by engine factories'
        raise NotImplementedError


    pass # end of AbstractComputingEngineFactory


# version
__id__ = "$Id$"

# End of file 
