#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2014  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from mcni.components.RadialCollimator import RadialCollimator as enginefactory, category

from mcni.pyre_support.AbstractComponent import AbstractComponent


class RadialCollimator( AbstractComponent ):

    __doc__ = enginefactory.__doc__

    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
        radius1 = pinv.float("radius1", default=0.3)
        radius2 = pinv.float("radius2", default=0.5)
        height1 = pinv.float("height1", default=0.5)
        height2 = pinv.float("height2", default=0.5)
        theta1 = pinv.float("theta1", default=0)
        theta2 = pinv.float("theta2", default=180)
        dtheta = pinv.float("dtheta", default=1)
        pass
    

    def process(self, neutrons):
        return self.engine.process( neutrons )


    def _configure(self):
        AbstractComponent._configure(self)
        return


    def _init(self):
        AbstractComponent._init(self)
        from math import pi
        si = self.inventory
        self.engine = enginefactory(
            self.name,
            si.radius1, si.height1,
            si.radius2, si.height2,
            si.theta1/180*pi, si.theta2/180*pi,
            si.dtheta/180*pi,
            )
        return

    pass # end of Source



# version
__id__ = "$Id$"

# End of file 
