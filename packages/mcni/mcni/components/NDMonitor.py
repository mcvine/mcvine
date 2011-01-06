#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class NDMonitor(object):

    def process(self, neutrons):
        from mcni.neutron_storage import neutrons_as_npyarr, ndblsperneutron
        arr = neutrons_as_npyarr(neutrons)
        arr.shape = -1, ndblsperneutron
        x = arr[:,0]; y = arr[:,1]; z = arr[:,2]
        vx = arr[:,3]; vy = arr[:,4]; vz = arr[:,5]
        t = arr[:,6]; 
        s1 = arr[:,7]; s2 = arr[:,8];
        p = arr[:,9]

        # propagate to z = 0
        self._propagateToZ0(x,y,z,vx,vy,vz,t)
        
        from numpy import histogramdd as hdd
        from mcni.utils import conversion
        sample = [eval(e) for e in self.expressions]
        bins = self.bins
        ranges = self.ranges
        self.histogram.I += hdd(sample, bins, ranges, weights=p)[0]
        self.histogram.E2 += hdd(sample, bins, ranges, weights=p*p)[0]
        return


    def _propagateToZ0(self, x,y,z, vx,vy,vz, t):
        dt = -z/vz
        x += vx*dt
        y += vy*dt
        z[:] = 0
        t += dt
        return


    def __init__(self, name, axes):
        """
        axes: a list of axis
        axis: a tuple of name, expression, bins, ranges
        name: name of the axis
        expression: expression of the axis
        bins: number of bins of the axis
        ranges: (min, max) tuple for the axis
        """
        self.name = name
        expressions = self.expressions = []
        bins = self.bins = []
        ranges = self.ranges = []
        haxes = []

        from histogram import histogram, axis
        from numpy import histogramdd as hdd, arange
        
        for n, e, b, r in axes:
            expressions.append(e)
            ranges.append(r)
            bins.append(b)
            db = (r[1]-r[0])/b
            a = axis(n, boundaries=arange(r[0], r[1]+db/10., db))
            haxes.append(a)
            continue
        self.histogram = histogram(self.name, haxes)
        return

    
    pass # end of NDMonitor


# version
__id__ = "$Id$"

# End of file 
