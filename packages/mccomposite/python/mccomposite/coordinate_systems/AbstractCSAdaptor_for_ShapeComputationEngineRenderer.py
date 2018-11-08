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


class AbstractCSAdaptor_for_ShapeComputationEngineRenderer:

    '''shape in mc simulation has some special conventions, we need
    this adaptor to make sure we are constructing shapes in ways
    that we really want.
    '''

    def onBlock(self, block):
        raise NotImplementedError

    def onCylinder(self, cylinder):
        raise NotImplementedError
    
    def onPyramid(self, pyramid):
        raise NotImplementedError
    
    def onCone(self, cone):
        raise NotImplementedError
    
    pass # end of AbstractCSAdaptor_for_ShapeComputationEngineRenderer


# version
__id__ = "$Id$"

# End of file 
