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
        x1,y1,z1 = self.intersectCylinder(
            (z,x,y), (vz,vx,vy), (self.radius1, self.height1))
        theta1 = np.atan(x1,y1) 
        x2,y2,z2 = self.intersectCylinder(
            (z,x,y), (vz,vx,vy), (self.radius2, self.height2))
        theta2 = np.atan(x2,y2)
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
        dtheta):
        self.name = name
        self.radius1 = radius1
        self.radius2 = radius2
        self.height1 = height1
        self.height2 = height2
        self.theta1 = theta1
        self.theta2 = theta2
        self.dtheta = dtheta
        return
    
    
    def intersectCylinder(self, position, velocity, cylinder):
        radius, height = cylinder
        x,y,z = position
        vx,vy,vz = velocity
        A = vx*vx + vy*vy
        B = 2*(x*vx + y*vy)
        C = x*x + y*y - radius*radius
        import numpy as np
        t = (np.sqrt(B*B-4*A*C) - B)/2/A
        return x+vx*t, y+vy*t, z+vz*t
    
    
    pass # end of MonochromaticSource


# version
__id__ = "$Id$"

# End of file 
