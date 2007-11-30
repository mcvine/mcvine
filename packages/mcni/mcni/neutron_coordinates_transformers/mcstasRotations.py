#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2005 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
handle rotation matrices

    - NAME: rotations

    - PURPOSE: provide methods to handle conversion between rotation angles
    and rotation matrices. McStas convention is used.

    - DESCRIPTION: In this simulation package, McStas convention is used
    to describe orientation of components. The orientation is represented
    by three consecutive rotations about x, y, z axis, with first rotation
    being one about x axis. The three axis are:

      z: incident neutron beam
      y: opposite to gravity
      x: perpendicular to z and y

    This module contains methods that handle conversion between rotation angles
    and rotation matrices. The rotation matrix returned converts coordinates
    in the original coordinate system to coordinates of the same vector
    in the rotated coordinate system.

    All rotation matrices follow the same convention: they convert coordinates
    from the original system to the rotated system.

    Example 1: the rotation matrix for a component (with respect to the
    instrument coords system) is m. The position of a neutron is r in the
    instrument coords system, then the position of this neutron in the component's
    coords sytem is:

      m * (r - r_comp)

    where r_comp is the position of the component in the instrument coords system.
    
    - RELATED: 

    - TODOs:
"""


from numpy import array,zeros,cos,sin, dot, transpose              
import numpy                                                                  


def toMatrix( *args, **kwds ):
    '''convert rotation angles to a rotation matrix.
the rotation matrix is related to
rotation angles phx, phy, phz as
    
  1. rotate around x axis by angle phx
  2. rotate around y axis by angle phy
  3. rotate around z axis by angle phz
    
this is actually a piece of c-code in mcstas.

Please be very careful and read the following texts to
understand the meaning of the matrix returned by this function.

Suppose we have a cartesian coordinate system CS.
Now, apply the rotations to this coordinate system
and we get another coordinate syste CS1.
Now a vector that is expressed as

  v = (vx, vy, vz)

in CS and

  v1 = (v1x, v1y, v1z)

in CS1. The relationship between v and v1 is

  v1 = m . v

So this rotation matrix is for rotating a coordinate system.

    '''
    usage = """toMatrix( 5, 6, 7, unit="deg")
    toMatrix( 5, 6, 7)
    toMatrix( (5,6,7), unit = "deg")
    toMatrix( (5, 6, 7) )
    """
    #if input is already a matrix, just return it
    if len(args) == 1 and isMatrix3(args[0]): return args[0]
    #otherwise we check if the input can be transformed to rotation angles
    if len(args) == 3: #phx, phy, phz
        angles = args
    elif len(args) == 1 and len(args[0]) == 3: # a tuple or list
        angles = args[0]
    else:
        raise SyntaxError, "Usage: %s" % usage
    return _toMatrix( angles[0], angles[1], angles[2], **kwds)
        

def _toMatrix(phx,phy,phz, unit='degree'):
    '''convert rotation angles to a rotation matrix.
    the rotation matrix is related to
    rotation angles phx, phy, phz as
    
    1. rotate around x axis by angle phx
    2. rotate around y axis by angle phy
    3. rotate around z axis by angle phz
    
    this is actually a piece of c-code in mcstas.
    '''
    if unit.lower()=='degree' or unit.lower()=='deg':
        phx = toradian( phx )
        phy = toradian( phy )
        phz = toradian( phz )
    cx = cos(phx);
    sx = sin(phx);
    cy = cos(phy);
    sy = sin(phy);
    cz = cos(phz);
    sz = sin(phz);
    t=zeros((3,3), float )
    t[0][0] = cy*cz;
    t[0][1] = sx*sy*cz + cx*sz;
    t[0][2] = sx*sz - cx*sy*cz;
    t[1][0] = -cy*sz;
    t[1][1] = cx*cz - sx*sy*sz;
    t[1][2] = sx*cz + cx*sy*sz;
    t[2][0] = sy;
    t[2][1] = -sx*cy;
    t[2][2] = cx*cy;
    return t
    
def toAngles(m, unit='degree'):
    '''convert a rotation matrix to angles. the rotation matrix is related to
    rotation angles phx, phy, phz as
    
    1. rotate around x axis by angle phx
    2. rotate around y axis by angle phy
    3. rotate around z axis by angle phz
    
    the conversion here follow similar treatment as those in
    http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToEuler/index.htm
    '''
    #if m is already a tuple of three rotation angles, just return it
    if isVector3(m): return m
    #otherwise we want to make sure m is a Matrix
    if not isMatrix3(m): raise TypeError , "Not a 3X3 matrix: %s" % m
    from numpy import arctan2, arcsin
    if m[2][0]>1-1e-8 :
        x=0.
        z=arctan2(m[0][1],m[1][1])
    elif m[2][0]<1e-8-1 :
        x=0.
        z=arctan2(m[0][1],m[1][1])
    else :
        z=arctan2(-m[1][0],m[0][0])
        x=arctan2(-m[2][1],m[2][2])
    y=arcsin(m[2][0])
    m1=toMatrix(x,y,z, unit = 'radian')
    try:
        for i in range(3):
            for j in range(3):
                if abs(m[i][j])<1e-8 :
                    if abs(m1[i][j]-m[i][j])>1e-8 :
                        raise 'conversion failed %s' % m
                else :
                    if abs( (m1[i][j]-m[i][j])/m[i][j] )>1e-8 :
                        raise 'conversion failed %s' % m
    except:
        print 'original matrix:',m
        print 'converted matrix:',m1
        raise 'conversion failed %s' % m
    if unit.lower() == 'deg' or unit.lower() == 'degree':
        return map(todegree, (x,y,z))
    else:
        return x,y,z


from utils import *


# version
__id__ = "$Id: mcstasRotations.py 1272 2007-10-27 13:25:13Z linjiao $"

# End of file 
