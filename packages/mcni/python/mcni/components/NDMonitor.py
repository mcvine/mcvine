#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                             Jiao Lin, Alex Dementsov
#                      California Institute of Technology
#                      (C) 2007-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
A powerful multi-dimensional monitor that 
can take various axes.
"""


category = "monitors"


class NDMonitor(object):    


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
        assert self.xwidth > 0 and self.yheight > 0

        # Filter
        ftr    = (x >= -self.xwidth/2)*(x <= self.xwidth/2)*(y >= -self.yheight/2)*(y <= self.yheight/2)

        x = x[ftr]; y = y[ftr]; z = z[ftr];
        vx = vx[ftr]; vy = vy[ftr]; vz = vz[ftr];
        s1 = s1[ftr]; s2 = s2[ftr]; t = t[ftr]; p = p[ftr];
        
        # after filtering, there might be no neutrons left
        if len(x) == 0:
            return
        
        from numpy import sqrt  # some expressions use 'sqrt()' function
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


    def __init__(self, name, axes, size=[0.1, 0.1]):
        """
        axes: a list of axis
        axis: an instance of Axis class, or 
            (obsolete) a tuple of name, expression, bins, range 
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
        self.xwidth     = size[0]
        self.yheight    = size[1]

        from histogram import histogram, axis as createAxis
        from numpy import histogramdd as hdd, arange

        # n='variable name', e='expression', b='number of bins (divisions)', r='range'
        for axis in axes:  
            if isinstance(axis, tuple):
                import warnings
                warnings.warn(
                    "It is obsolete to specify an axis using tuple. "
                    "Please use an Axis instance instead"
                    )
                n, e, b, r = axis
                unit = None
            else:
                n = axis.name
                e = axis.expression
                b = axis.bins
                r = axis.range
                unit = axis.unit
                
            # validation
            if len(r) != 2:
                raise ValueError("Invalid range: %s. A range has to be a 2-tuple" % (r, ))
            if r[0] >= r[1]:
                raise ValueError("Invalid range: %s" % (r,))
            
            expressions.append(e)
            ranges.append(r)
            bins.append(b)
            db = (r[1]-r[0])/b
            a = createAxis(
                n, 
                boundaries=arange(r[0], r[1]+db/10., db), 
                unit=unit)
            haxes.append(a)
            continue
        self.histogram = histogram(self.name, haxes)
        return

    
    pass # end of NDMonitor


    # this is the required interface to supply an axis
    # to the constructor
class Axis(object):
    # name of axis
    name = '' 
    # evaluation expression
    expression = ''
    # number of bins
    bins = 0
    # range (min, max)
    range = (0, 0)

    def __init__(self, **kwds):
        for k,v in kwds.items():
            setattr(self, k, v)


# version
__id__ = "$Id$"

# End of file 
