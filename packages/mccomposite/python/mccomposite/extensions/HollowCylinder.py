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


class HollowCylinder:
    
    def __init__(self, in_radius, out_radius, height):
        self.in_radius = in_radius
        self.out_radius = out_radius
        self.height = height
        return
    
    def identify(self, visitor): return visitor.onHollowCylinder(self)
    
    pass # HollowCylinder


# handler of computation engine renderer for HollowCylinder
def onHollowCylinder(self, hollowCylinder):
    from mccomposite.geometry.primitives import cylinder
    from mccomposite.geometry.operations import subtract
    r1 = hollowCylinder.in_radius
    r2 = hollowCylinder.out_radius
    if r1 >= r2:
        msg = 'inner radius (%s) should be smaller than outer radius (%s)' %(
            r1, r2)
        raise RuntimeError(msg)

    h = hollowCylinder.height
    if r1 == 0*r1:
        shape = cylinder(r2, h)
    else:
        shape = subtract( cylinder( r2, h ), cylinder(r1,h*2) )
    return shape.identify(self)


# 4. register the new class and handlers
import mccomposite.geometry
mccomposite.geometry.register_engine_renderer_handler(HollowCylinder, onHollowCylinder)


# version
__id__ = "$Id$"

# End of file 
