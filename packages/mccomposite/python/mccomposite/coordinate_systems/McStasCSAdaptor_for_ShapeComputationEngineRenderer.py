#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


class McStasCSAdaptor_for_ShapeComputationEngineRenderer:

    '''shape in mc simulation has some special conventions, we need
    this adaptor to make sure we are constructing shapes in ways
    that we really want.

    The objects handled by this class is implemented in instrument.geometry.shapes
    and instrument.geometry.operations

    This class is combined with mccomposite.geometry.ShapeComputationEngineRenderer
    in mccomposite.scattererEngine to render c++ instances from python instances.
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

    def onPyramid(self, pyramid):
        p = self._remove_length_unit( (pyramid.thickness, pyramid.width, pyramid.height) )
        solid = self.factory.pyramid( *p )
        # pyramid should have vertical axis. (y axis)
        # but the pyramid created above is along z axis. need to rotate -90 about x axis
        r = self.factory.orientation( (-90,0,0) )
        solid = self.factory.rotate( solid, r )
        # and then rotate along y by -90.
        r = self.factory.orientation( (0, -90, 0) )
        solid = self.factory.rotate(solid, r)
        return solid

    def onCone(self, cone):
        p = self._remove_length_unit( (cone.radius, cone.height) )
        solid = self.factory.cone( *p )
        # cone should have vertical axis. (y axis)
        # but the cone created above is along z axis. need to rotate -90 about x axis
        r = self.factory.orientation( (-90,0,0) )
        solid = self.factory.rotate( solid, r )
        return solid

    def onCylinder(self, cylinder):
        p = self._remove_length_unit( (cylinder.radius, cylinder.height) )
        cyl = self.factory.cylinder( *p )
        # cylinder should have vertical axis. (y axis)
        # but the cylinder created above is along z axis. need to rotate -90 about x axis
        r = self.factory.orientation( (-90,0,0) )
        return self.factory.rotate( cyl, r )

    def onTranslation(self, translation):
        vector = translation.vector
        if not translation.implicit_coordinate_system:
            beam, transversal, vertical = vector
            vector = (transversal, vertical, beam)
        body  = translation.body.identify(self)
        v = self._remove_length_unit( vector )
        offset = self.factory.position( v )
        return self.factory.translate(body, offset)
    
    def onRotation(self, rotation):
        if rotation.euler_angles is not None:
            orientation = self._remove_angle_unit(rotation.euler_angles)
        else:
            axis = rotation.axis
            if not rotation.implicit_coordinate_system:
                beam, transversal, vertical = axis
                axis = transversal, vertical, beam
            angle = self._remove_angle_unit(rotation.angle)
            orientation = axis, angle
        rotmat = self.factory.orientation(orientation)
        body = rotation.body.identify(self)
        return self.factory.rotate(body, rotmat)

    pass # end of McStasCSAdaptor_for_ShapeComputationEngineRenderer


# End of file 
