#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


class SphereShell:
    
    def __init__(self, in_radius, out_radius):
        self.in_radius = in_radius
        self.out_radius = out_radius
        return
    
    def identify(self, visitor): return visitor.onSphereShell(self)
    
    pass # SphereShell


# handler of computation engine renderer for SphereShell
def onSphereShell(self, sphereShell):
    from mccomposite.geometry.primitives import sphere
    from mccomposite.geometry.operations import subtract
    r1 = sphereShell.in_radius
    r2 = sphereShell.out_radius
    if r1 >= r2:
        msg = 'inner radius (%s) should be smaller than outer radius (%s)' %(
            r1, r2)
        raise RuntimeError, msg

    if r1 == 0*r1:
        shape = sphere(r2)
    else:
        shape = subtract( sphere(r2), sphere(r1) )
    return shape.identify(self)


# 4. register the new class and handlers
import mccomposite.geometry
mccomposite.geometry.register_engine_renderer_handler(SphereShell, onSphereShell)


# End of file 
