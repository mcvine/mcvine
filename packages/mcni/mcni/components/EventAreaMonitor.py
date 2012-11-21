#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2012  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
event mode area detector

detector has an area in
[xmin, xmax) X [ymin, ymax)
and accepts neutrons in tof region [tmin, tmax)

detector is divided to pixels nx X ny

total tof bins: nt

The detector will generate a data file with events
saved as numpy array. 
Its data structure is defined in mccomponents.detector.event_utils.

pixelID: x_index*ny + y_index (this is so because y is normally vertical along detector tube)
tofChannelNo: tof_index
p: probability
"""


category = "monitors"


class EventAreaMonitor(object):    


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
        
        # propagate to z = 0
        self._propagateToZ0(x,y,z,vx,vy,vz,t)

        # Apply filter if area is positive
        assert self.xmax > self.xmin and self.ymax > self.ymin and self.tmax > self.tmin
        
        # Filter
        ftr    = (x >= self.xmin)*(x < self.xmax)*(y >= self.ymin)*(y < self.ymax)*(t >= self.tmin)*(t<self.tmax)
        
        x = x[ftr]
        # after filtering, there might be no neutrons left
        if len(x) == 0:
            return
        
        y = y[ftr]; z = z[ftr];
        # vx = vx[ftr]; vy = vy[ftr]; vz = vz[ftr];
        # s1 = s1[ftr]; s2 = s2[ftr]; 
        t = t[ftr]; p = p[ftr];
        
        # create empty events
        from mccomponents.detector import event_utils
        import numpy
        events = numpy.zeros(x.size, dtype=event_utils.datatype)
        
        # x,y
        dx = (self.xmax-self.xmin)/self.nx
        x_index = (x-self.xmin)/dx
        dy = (self.ymax-self.ymin)/self.ny
        y_index = (y-self.ymin)/dy
        events['pixelID'] = x_index * self.ny + y_index
        # t
        dt = (self.tmax-self.tmin)/self.nt
        events['tofChannelNo'] = (t-self.tmin)/dt
        # p
        events['p'] = p
        
        self.events = events
        return
    

    def _propagateToZ0(self, x,y,z, vx,vy,vz, t):
        dt = -z/vz
        x += vx*dt
        y += vy*dt
        z[:] = 0
        t += dt
        return


    def __init__(
        self, name, 
        xmin=-0.1, xmax=0.1, ymin=-0.1, ymax=0.1, 
        tmin=0.0, tmax=0.01,
        nx = 100, ny = 100, nt=100,
        ):
        """
        """
        self.name = name
        self.xmin = xmin
        self.xmax = xmax
        self.nx = nx
        self.ymin = ymin
        self.ymax = ymax
        self.ny = ny
        self.tmin = tmin
        self.tmax = tmax
        self.nt = nt
        return
    
    
    pass # end of EventAreaMonitor


# version
__id__ = "$Id: NDMonitor.py 1144 2011-04-28 04:02:13Z linjiao $"

# End of file 
