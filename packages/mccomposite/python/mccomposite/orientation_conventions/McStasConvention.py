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


from mcni.neutron_coordinates_transformers import mcstasRotations as mr


from AbstractOrientationConvention import AbstractOrientationConvention as base
class McStasConvention(base):

    """convert rotation angles to rotation matrix using mcstas convention

    Rotation angles:
      (rx,ry,rz)
      Three consecutive rotations about x,y,z axes

    Rotation matrix:
      The rotation matrix's inverse will convert coordinates of
      a vector in the hosts's coordinate system to the element's coordinate
      system. The element's orientation is described by the three rotations.
    """

    def angles2matrix(self, angles):
        x,y,z = angles
        return mr.toMatrix(x,y,z, unit='deg').T

    pass # end of McstasConvention


# version
__id__ = "$Id$"

# End of file 
