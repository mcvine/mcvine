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


class AbstractBinding:


    def compositescatterer(self, shape, elements, geometer):
        raise NotImplementedError


    def scatterercontainer(self):
        raise NotImplementedError


    def geometer(self):
        raise NotImplementedError
    

    def position(self, x,y,z):
        """create binding's representation of position vector
        """
        raise NotImplementedError


    def orientation(self, rotmat):
        """convert rotation matrix numpy instance to binding\'s representation
        of rotation matrix
        """
        raise NotImplementedError


    def unite(self, shapes):
        raise NotImplementedError

    def intersect(self, shapes):
        raise NotImplementedError

    def subtract(self, shape1, shape2):
        raise NotImplementedError

    def dilate(self, shape, scale):
        raise NotImplementedError

    def rotate(self, shape, rotmat):
        raise NotImplementedError

    def translate(self, shape, vector):
        raise NotImplementedError

    def block(self, diagonal):
        raise NotImplementedError

    def sphere(self, radius):
        raise NotImplementedError

    def cylinder(self, radius, height):
        raise NotImplementedError
        
    pass # end of AbstractBinding


# version
__id__ = "$Id$"

# End of file 
