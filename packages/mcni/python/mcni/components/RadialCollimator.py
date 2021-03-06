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


category = 'optics'


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
            * (theta1 > self.theta1) * (theta1 < self.theta2) \
            * (theta2 > self.theta1) * (theta2 < self.theta2) \
            * ((theta1-self.theta1)//self.dtheta == (theta2-self.theta1)//self.dtheta)
        good = arr[good, :]
        
        neutrons.resize(good.shape[0], neutrons[0])
        neutrons.from_npyarr(good)
        return
    
    
    def __init__(
        self, name, 
        radius1, height1, radius2, height2,
        theta1, theta2, 
        dtheta, oscillation=0):
        self.name = name
        self.radius1 = radius1
        self.radius2 = radius2
        self.height1 = height1
        self.height2 = height2
        self.theta1 = theta1
        self.theta2 = theta2
        self.dtheta = dtheta
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


import numpy as np


def test():
    DEG2RAD = np.pi/180
    from mcni import neutron_buffer, neutron
    neutrons = neutron_buffer(1)
    coll = RadialCollimator(
        name="collimator",
        radius1=0.308, height1=0.6, radius2=0.462, height2=0.6,
        theta1=-30*DEG2RAD, theta2=150*DEG2RAD, 
        dtheta=1.6*DEG2RAD)
    def check(neutron, absorbed):
        neutrons.resize(1, neutron)
        neutrons[0] = neutron
        coll.process(neutrons)
        assert len(neutrons) == (not absorbed)
        return
    
    check(neutron(r=(0,0,0), v=(-0.9,0,1.732), prob=1), False)
    check(neutron(r=(0,0,0), v=(-1.1,0,1.732), prob=1), True)
    check(neutron(r=(0,0,0), v=(0,-0.3,0.463), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,-0.3,0.461), prob=1), True)
    check(neutron(r=(0,0,0), v=(0,0.3,0.463), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,0.3,0.461), prob=1), True)
    check(neutron(r=(0,0,0), v=(0.1,0.3,0.45), prob=1), True)
    check(neutron(r=(0,0,0), v=(0.1,0.3,0.462), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,0,1000), prob=1), False)
    check(neutron(r=(0,0,0), v=(1000,0,0), prob=1), False)
    check(neutron(r=(0,0,0), v=(1000,0,-1000), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,0,-1000), prob=1), True)
    check(neutron(r=(0.1,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.001,0,0), v=(0,0,1000), prob=1), False)
    check(neutron(r=(0.01,0,0), v=(0,0,1000), prob=1), False)
    check(neutron(r=(0.03,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.025,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.015,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.1,0,0), v=(0,10,0), prob=1), True)
    for i in range(10):
        check(neutron(r=(0,0,0), v=(1,0,i), prob=1), False)
    for i in range(1,10):
        check(neutron(r=(0,0,0), v=(i,0,-1), prob=1), False)
        continue
    return


if __name__ == '__main__': test()
    

# version
__id__ = "$Id$"

# End of file 
