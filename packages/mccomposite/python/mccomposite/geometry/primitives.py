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

from pyre.geometry.solids import *

def pyramid(*args):
    return Pyramid(*args)

def cone(*args):
    return Cone(*args)

from pyre.geometry.solids.Cylinder import Cylinder
from pyre.geometry.solids.Block import Block
from pyre.geometry.solids.Sphere import Sphere
from instrument.geometry.shapes.Pyramid import Pyramid
from instrument.geometry.shapes.Cone import Cone

# version
__id__ = "$Id$"

# End of file 
