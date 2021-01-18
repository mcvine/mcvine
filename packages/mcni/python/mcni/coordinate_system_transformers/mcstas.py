#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                  Jiao  Lin
#                        California Institute of Technology
#                        (C) 2006-2010  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 


'''
This implements the mcstas transformer for 
..AbstractCoordinateSystemTransformer

The implementation here is closely related to 
..neutron_coordinates_transformers.mcstas
'''


from numpy import dot, array, mat
from mcni.neutron_coordinates_transformers.mcstasRotations import toMatrix
def transformCoordinateSystem(obj1abspos, obj1absori, obj2relpos, obj2relori):
    obj1absori = toMatrix(obj1absori)
    obj2relori = toMatrix(obj2relori)
    pos = obj1abspos + dot(obj1absori.T, obj2relpos)
    ori = mat(obj2relori) * mat(obj1absori)
    return pos, ori



def test_template(obj1abspos, obj1absori, obj2abspos, obj2absori):
    from mcni.neutron_coordinates_transformers import mcstas
    print('obj1 absolute pos, ori:',  obj1abspos, obj1absori)
    print('obj2 absolute pos, ori:',  obj2abspos, obj2absori)

    obj2relpos, obj2relori = mcstas.relativePositionOrientation( 
        obj1abspos, obj1absori, obj2abspos, obj2absori,
        )
    print('relative pos, ori:', obj2relpos, obj2relori)
    
    obj2abspos_, obj2absori_ = transformCoordinateSystem(
        obj1abspos, obj1absori, obj2relpos, obj2relori)
    
    print('computed absolute pos, ori:', obj2abspos_, obj2absori_)
    
    import numpy.testing as nt
    nt.assert_array_almost_equal(obj2abspos, obj2abspos_)
    nt.assert_array_almost_equal(obj2absori, obj2absori_)
    
    return


def test():
    obj1abspos, obj1absori = (0,0,0), array(((1,0,0),
                                             (0,1,0),
                                             (0,0,1)))
    obj2abspos, obj2absori = (0,0,1), array(((0,1,0),
                                             (-1,0,0),
                                             (0,0,1)))
    test_template(obj1abspos, obj1absori,
                  obj2abspos, obj2absori)

    obj1abspos, obj1absori = (0,0,1), array(((0,1,0),
                                             (-1,0,0),
                                             (0,0,1)))
    obj2abspos, obj2absori = (0,0,0), array(((1,0,0),
                                             (0,1,0),
                                             (0,0,1)))
    test_template(obj1abspos, obj1absori,
                  obj2abspos, obj2absori)

    from mcni.neutron_coordinates_transformers.mcstasRotations import toMatrix
    obj1abspos, obj1absori = (0,0,1), toMatrix(0, 90, 90)
    obj2abspos, obj2absori = (0,0,0), toMatrix(90,0,90)
    test_template(obj1abspos, obj1absori,
                  obj2abspos, obj2absori)
    return


def test2_template(absr1, relr2, expected_absr2):
    from mcni.neutron_coordinates_transformers.mcstasRotations import toMatrix, toAngles
    obj1abspos, obj1absori = (0,0,0), toMatrix(*absr1)
    obj2relpos, obj2relori = (0,0,0), toMatrix(*relr2)
    obj2abspos, obj2absori = transformCoordinateSystem(
        obj1abspos, obj1absori, obj2relpos, obj2relori)
    r = toAngles(array(obj2absori))
    import numpy.testing as nt
    nt.assert_array_almost_equal( r, expected_absr2 )
    return    


def test2():
    test2_template((10,0,0), (5,0,0), (15,0,0))
    test2_template((10,0,0), (15,0,0), (25,0,0))
    test2_template((0,10,0), (0,5,0), (0,15,0))
    test2_template((0,10,0), (0,15,0), (0,25,0))
    test2_template((0,0,10), (0,0,5), (0,0,15))
    test2_template((0,0,10), (0,0,15), (0,0,25))

    test2_template((90, 0, 0), (0, 30, 0), (90, 30, 0))
    test2_template((0, 0, 90), (0, 90, 0), (-90, 0, 90))
    test2_template((31, 0, 0), (0, 22, 0), (31, 22, 0))
    test2_template((0, 31, 0), (0, 0, 22), (0, 31, 22))
    test2_template((31, 0, 0), (0, 0, 22), (31, 0, 22))
    return    


def main():
    test()
    test2()
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

#  End of file 
