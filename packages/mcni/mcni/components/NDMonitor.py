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


category = 'monitors'


from mcni.AbstractComponent import AbstractComponent

class NDMonitor( AbstractComponent ):

    def process(self, neutrons):
        from mcni.neutron_storage import neutrons_as_npyarr, ndblsperneutron
        arr = neutrons_as_npyarr(neutrons)
        arr.shape = -1, ndblsperneutron
        x = arr[:,0]; y = arr[:,1]; z = arr[:,2]
        vx = arr[:,3]; vy = arr[:,4]; vz = arr[:,5]
        t = arr[:,6]; 
        s1 = arr[:,7]; s2 = arr[:,8];
        p = arr[:,9]
        from numpy import histogramdd as hdd
        sample = [eval(e) for e in self.expressions]
        bins = self.bins
        ranges = self.ranges
        self.histogram.I += hdd(sample, bins, ranges, weights=p)[0]
        self.histogram.E2 += hdd(sample, bins, ranges, weights=p*p)[0]
        return


    def __init__(self, name, expressions, bins, ranges):
        """
        expressions: expressions of all dimensions. a list of length D
        bins: a sequence of number of bins, each for one dimension.
        ranges: a sequence of tuples. each tuple is (min, max) that specify the range
        """
        self.name = name
        self.expressions = expressions
        self.bins = bins
        self.ranges = ranges
        from histogram import histogram, axis
        axes = []
        from numpy import histogramdd as hdd, arange
        for e, b, r in zip(expressions, bins, ranges):
            db = (r[1]-r[0])/b
            a = axis(e, boundaries=arange(r[0], r[1]+db/10., db))
            axes.append(a)
            continue
        self.histogram = histogram(name, axes)
        return

    
    pass # end of NDMonitor


# version
__id__ = "$Id$"

# End of file 
