#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# functions to create dos histogram from files

def doshist_fromidf(datapath):
    "read dos histogram from a idf data file"
    from mccomponents.sample.idf import readDOS
    e,Z = readDOS(datapath)
    from histogram import histogram
    return histogram( 'dos', [ ('energy', e, 'meV') ], data = Z )


def doshist_fromascii(datapath, x_unit=None):
    "read dos histogram from an ascii data file"
    import warnings, numpy as np
    # read data 
    lines = open(datapath)
    data = []; comments = []
    for line in lines:
        line = line.strip()
        if not line: continue
        if line[0] == '#':
            comments.append(line[1:])
            continue
        tokens = line.split()
        try:
            numbers = map(float, tokens)
        except Exception as e:
            msg = 'Skip line %s' % line
            warnings.warn(msg)
            continue
        data.append(numbers)
        continue
    # treat data
    data = np.array(data).T
    E,I = data[:2]
    if len(data)>2:
        errorsq = data[2] **2
    else:
        errorsq = None
    # try to get unit information from comments
    supported_units = ['meV', 'TeraHz']
    if comments:
        found = False
        for c in comments:
            tokens = c.strip().split()
            desc = tokens[0] # description of x axis
            for u in supported_units:
                if desc.find(u) != -1:
                    x_unit = u
                    found = True
                    break
                continue
            if found: break
            continue
    # unit conversion
    if x_unit == 'meV': pass
    elif x_unit == 'TeraHz': 
        from .units import hertz2mev
        from math import pi
        E *= 2*pi*1e12 * hertz2mev
    else:
        raise NotImplementedError("energy unit: %s" % x_unit)
    from histogram import histogram
    axes = [('energy', E, 'meV')]
    return histogram( 'dos', axes, data = I, errors = errorsq)


# functions to create dos data objects from data files

def dos_fromidf(datapath):
    doshist = doshist_fromidf(datapath)
    return dos_fromdoshist(doshist)


def dos_fromh5(datapath):
    import histogram.hdf as hh
    dos = hh.load(datapath)
    return dos_fromdoshist(dos)
    

def dos_fromascii(datapath, **kwds):
    dh = doshist_fromascii(datapath, **kwds)
    return dos_fromdoshist(dh)


# helpers
def dos_fromdoshist(h):
    from .LinearlyInterpolatedDOS import LinearlyInterpolatedDOS as f
    return f(h)
    

# version
__id__ = "$Id$"

# End of file 
