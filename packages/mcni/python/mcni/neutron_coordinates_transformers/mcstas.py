
from .mcstasRotations import toMatrix
from numpy import array, dot, mat

def relativePositionOrientation(
    position1, orientation1,
    position2, orientation2 ):

    rotmat2 = toMatrix( orientation2, unit = 'degree' )
    rotmat1 = toMatrix( orientation1, unit = 'degree' )
    
    m = mat(rotmat2) * mat(rotmat1.T)
    m = array(m)

    position1 = array(position1)
    position2 = array(position2)

    r12abs = position2 - position1

    r = dot(rotmat1, r12abs)
    return r, m
