#
# https://stackoverflow.com/questions/6802577/rotation-of-3d-vector

import numpy as np, math

def matrix_rotationaboutaxis(axis, theta):
    """
    Return the rotation matrix associated with clockwise rotation about
    the given axis by theta degrees.
    """
    theta = np.deg2rad(theta)
    axis = np.asarray(axis)
    axis = axis/math.sqrt(np.dot(axis, axis))
    a = math.cos(theta/2.0)
    b, c, d = axis*math.sin(theta/2.0)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    return np.array(
        [[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
         [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
         [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]
        ])

