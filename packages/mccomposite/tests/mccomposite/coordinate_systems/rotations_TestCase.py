#!/usr/bin/env python
#
#


import unittest, numpy as np

class TestCase(unittest.TestCase):

    def test(self):
        from mccomposite.coordinate_systems import rotations
        from mcni.neutron_coordinates_transformers import mcstasRotations as mr
        np.allclose(
            rotations.matrix_rotationaboutaxis((1,0,0), np.pi/2.),
            mr.toMatrix(90., 0, 0, unit='deg')
            )
        np.allclose(
            rotations.matrix_rotationaboutaxis((0,1,0), np.pi/2.),
            mr.toMatrix(0., 90, 0, unit='deg')
            )
        np.allclose(
            rotations.matrix_rotationaboutaxis((0,0,1), np.pi/2.),
            mr.toMatrix(0., 0, 90, unit='deg')
            )
        
        np.allclose(
            rotations.matrix_rotationaboutaxis((1,1,1), np.pi/180.*120.),
            mr.toMatrix(90., 90, 0, unit='deg')
            )


if __name__ == "__main__": unittest.main()
    
# End of file 
