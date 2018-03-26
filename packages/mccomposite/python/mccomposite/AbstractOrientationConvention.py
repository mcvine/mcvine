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


class AbstractOrientationConvention:

    """convert orientation to rotation matrix
    """

    def tomatrix(self, orientation):
        """orientation can be a 3-tuple of angles,
        or it can be a 2-tuple of (axis, angle)

        angles are all in degrees
        """
        if len(orientation)==3:
            # 3 angles
            return self.eulerToMatrix(orientation)
        elif len(orientation)==2:
            # axis and angle
            axis, angle = orientation
            return self.axis_and_angle_ToMatrix(axis, angle)
        raise ValueError("Unknown input: %s" % orientation)

    def eulerToMatrix(self, angles):
        raise NotImplementedError

    def axis_and_angle_ToMatrix(self, axis, angle):
        raise NotImplementedError

    pass # end of AbstractOrientationConvention


# version
__id__ = "$Id$"

# End of file 
