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


class InstrumentScientistCSAdaptor_for_ShapeComputationEngineRenderer:

    '''shape in mc simulation has some special conventions, we need
    this adaptor to make sure we are constructing shapes in ways
    that we really want.
    '''

    def onBlock(self, block):
        # x: downstream. thickness
        # y: horizontal. width
        # z: vertical up. height
        try: diagonal = block.diagonal
        except:
            diagonal = block.thickness, block.width, block.height
            pass
        diagonal = self._remove_length_unit( diagonal )
        return self.factory.block( diagonal )

    def onPyramid(self, pyramid):
        # x: downstream. thickness
        # y: horizontal. width
        # z: vertical up. height
        xyz = pyramid.thickness, pyramid.width, pyramid.height
        xyz = self._remove_length_unit( xyz )
        return self.factory.pyramid( *xyz )

    def onCylinder(self, cylinder):
        p = self._remove_length_unit( (cylinder.radius, cylinder.height) )
        return self.factory.cylinder( *p )

    pass # end of InstrumentScientistCSAdaptor_for_ShapeComputationEngineRenderer


# version
__id__ = "$Id$"

# End of file 
