#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
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
        theta1 = pinv.float("theta1", default=None)
        theta2 = pinv.float("theta2", default=None)
        dtheta = pinv.float("dtheta", default=None)
        theta_list = pinv.array("theta_list", default=None)
        oscillation = pinv.float("oscillation", default=1)
        pass

    def process(self, neutrons):
        return self.engine.process( neutrons )

    def _configure(self):
        AbstractComponent._configure(self)
        return

    def _init(self):
        AbstractComponent._init(self)
        from math import pi
        import numpy as np
        si = self.inventory
        self.engine = enginefactory(
            self.name,
            si.radius1, si.height1,
            si.radius2, si.height2,
            si.theta1/180*pi if si.theta1 is not None else None,
            si.theta2/180*pi if si.theta2 is not None else None,
            si.dtheta/180*pi if si.dtheta is not None else None,
            np.array(si.theta_list)*(pi/180) if si.theta_list is not None else None,
            si.oscillation/180*pi,
            )
        return

    pass # end of Source

# End of file
