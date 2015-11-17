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


class AbstractNeutronCoordinatesTransformer:


    '''base class of coordinates transformers

    This functor first calculates the postion vector and the orientation
    matrix, and then apply them to transform the given neutrons.

    The two steps need two operators:

    1. relative positon and orientation from absolute positions and
    orientations. This depends on coordinate system and the repersentation
    convention of orientation matrix.

    2. apply offset vector and rotation matrix to neutrons. This depends
    on the type of the neutron_buffer object.
    '''

    # calcualte relative position vector and orientation rotation matrix
    # given absolute positions and orientations of two objects.
    relativePositionOrientation = None 

    # apply offset vector and rotation matrix
    applyOffsetRotation = None
    
    
    def __call__(self, neutrons,
                 oldposition, oldorientation,
                 newposition, neworientation):
        '''transform neutron coordinates from old coordinate system
        to new coordinate system.

        The position and orientation of the old coordinate system
        is given by  oldposition, oldorientation.

        The position and orientation of the new coordinate system
        is given by  newposition, neworientation
        
        '''
        offset, rotation = self.relativePositionOrientation(
            oldposition, oldorientation,
            newposition, neworientation)

        self.applyOffsetRotation( offset, rotation, neutrons )
        return


    pass # AbstractCoordinatesTransformer


# version
__id__ = "$Id$"

# End of file 
