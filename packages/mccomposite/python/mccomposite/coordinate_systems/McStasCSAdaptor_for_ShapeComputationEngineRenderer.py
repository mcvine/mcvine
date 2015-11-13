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


class McStasCSAdaptor_for_ShapeComputationEngineRenderer:

    '''shape in mc simulation has some special conventions, we need
    this adaptor to make sure we are constructing shapes in ways
    that we really want.
    '''

    def onBlock(self, block):
        # x: horizontal. width
        # y: vertical up. height
        # z: downstream. thickness
        try: diagonal = block.diagonal
        except:
            diagonal = block.width, block.height, block.thickness
            pass
        diagonal = self._remove_length_unit( diagonal )
        return self.factory.block( diagonal )

    def onCylinder(self, cylinder):
        p = self._remove_length_unit( (cylinder.radius, cylinder.height) )
        cyl = self.factory.cylinder( *p )
        # cylinder should have vertical axis. (y axis)
        # but the cylinder created above is along z axis. need to rotate -90 about x axis
        r = self.factory.orientation( (-90,0,0) )
        return self.factory.rotate( cyl, r )

    pass # end of McStasCSAdaptor_for_ShapeComputationEngineRenderer


# version
__id__ = "$Id$"

# End of file 
