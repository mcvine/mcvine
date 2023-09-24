#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

category = 'optics'

import numpy as np
from mcni.AbstractComponent import AbstractComponent

class RadialCollimator( AbstractComponent ):

    def process(self, neutrons):
        if not len(neutrons):
            return
        from mcni.neutron_storage import neutrons_as_npyarr, ndblsperneutron
        arr = neutrons_as_npyarr(neutrons)
        arr.shape = -1, ndblsperneutron
        x = arr[:,0]; y = arr[:,1]; z = arr[:,2]
        vx = arr[:,3]; vy = arr[:,4]; vz = arr[:,5]
        s1 = arr[:,6]; s2 = arr[:,7];
        t = arr[:,8];
        p = arr[:,9]
        #
        theta_osc = self.oscillation * np.random.rand(len(neutrons))
        x1,y1,z1 = self.intersectCylinder(
            (z,x,y), (vz,vx,vy), (self.radius1, self.height1))
        theta1 = np.arctan2(y1,x1)  + theta_osc
        x2,y2,z2 = self.intersectCylinder(
            (z,x,y), (vz,vx,vy), (self.radius2, self.height2))
        theta2 = np.arctan2(y2,x2) + theta_osc
        good = (x1==x1) \
            * (z1<self.height1/2.) * (z1>-self.height1/2.) \
            * (z2<self.height2/2.) * (z2>-self.height2/2.) \
            * (theta1 > self.theta_min) * (theta1 < self.theta_max) \
            * (theta2 > self.theta_min) * (theta2 < self.theta_max)
        if self.dtheta is not None:
            good *= (theta1-self.theta_min)//self.dtheta == (theta2-self.theta_min)//self.dtheta
        else:
            good *= np.digitize(theta1, self.theta_list) == np.digitize(theta2, self.theta_list)
        good = arr[good, :]
        neutrons.resize(good.shape[0], neutrons[0])
        neutrons.from_npyarr(good)
        return

    def __init__(
            self, name,
            radius1, height1, radius2, height2,
            # theta1=0, theta2=np.pi, dtheta=np.radians(10),
            theta1=None, theta2=None, dtheta=None,
            theta_list = None,
            oscillation=0
    ):
        """Radial collimator
        radius1, height1: radius and height of inner cylinder
        radius2, height2: radius and height of outer cylinder
        theta1, theta2, dtheta: use these for evenly spaced blade locations
        theta_list: use this for arbitrarily spaced blade locations. must be increasing
        all angles are in radians
        """
        self.name = name
        self.radius1 = radius1
        self.radius2 = radius2
        self.height1 = height1
        self.height2 = height2
        if theta1 is not None and theta2 is not None and dtheta is not None:
            self.theta_min = theta1
            self.theta_max = theta2
            self.dtheta = dtheta
        else:
            self.theta_min = theta_list[0]
            self.theta_max = theta_list[-1]
            self.theta_list = theta_list
            self.dtheta = None
        self.oscillation = oscillation
        return

    def intersectCylinder(self, position, velocity, cylinder):
        radius, height = cylinder
        x,y,z = position
        vx,vy,vz = velocity
        A = vx*vx + vy*vy
        B = 2*(x*vx + y*vy)
        C = x*x + y*y - radius*radius
        t = (np.sqrt(B*B-4*A*C) - B)/2/A
        return x+vx*t, y+vy*t, z+vz*t

    pass # end of MonochromaticSource


# End of file
