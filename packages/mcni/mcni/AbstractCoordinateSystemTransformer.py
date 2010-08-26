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


class AbstractCoordinateSystemTransformer:


    '''this defines the interface of the "coordinate system transformer"

    Given the absolute position and orientation of object 1,
    and relative position and orientation of object 2,
    computes the absolute position and orientation of object 2.
    '''

    
    def __call__(self, obj1abspos, obj1absori, obj2relpos, obj2relori):
        raise NotImplementedError


    pass # AbstractCoordinateSystemTransformer


# version
__id__ = "$Id$"

# End of file 
