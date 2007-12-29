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

from pyre.geometry.operations import *


#overload union and intersection to allow more-than-two elements
from pyre.geometry.operations.Composition import Composition as base
class Composition(base):

    def __init__(self, *shapes):
        self.shapes = shapes
        return


class Union(Composition):
    def identify(self, visitor): return visitor.onUnion(self)
    pass


class Intersection(Composition):
    def identify(self, visitor): return visitor.onIntersection(self)
    pass


#overload rotation
from pyre.geometry.operations.Rotation import Rotation as base
class Rotation(base):

    def __init__(self, body, angles):
        self.body = body
        self.angles = angles
        return



def unite(*shapes):
    return Union(*shapes)


def intersect(*shapes):
    return Intersection(*shapes)


def rotate(shape, angles):
    return Rotation(shape, angles)


# version
__id__ = "$Id$"

# End of file 
