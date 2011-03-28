#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def events2Ipixtof( events, ipixtof ):
    for pix,tof, n in events:
        ipixtof[ pix, tof ] += n
        continue
    return


import pyre.units.length
import pyre.units.energy
import pyre.units.time

def events2IQE(
    eventsfile, nevents, 
    pixelpositionsfile, npixels,
    mod2sample=13.6*pyre.units.length.meter, Ei=100*pyre.units.energy.meV,
    Qaxis=(0,10,0.1), Eaxis=(-95,95,1.),
    tofUnit=100*pyre.units.time.ns,
    toffset=0*pyre.units.time.s,
    tofmax=0.015*pyre.units.time.s,
    ):
    '''
    direct geometery inelastic neutron scattering reduction
    
    vf = r(pixel) / (t-t1)

    r(pixel): distance from smaple to pixel
    t: tof
    t1: time from source to sample
    
    E = Ei - Ef
    Q = ki - kf

    vi = (0, 0, vi)

    t1 = mod2sample / vi

    eventsfile: events file
    nevents: number of events
    pixelpositionsfile:  unit:meter
    npixels:
    mod2sample: moderator to sample distance 
    Ei: incident energy
    Qaxis, Eaxis: (min, max, step) of Q and E
    '''
    if not isinstance(eventsfile, basestring):
        raise ValueError, "%s is not a str" % eventsfile
    import os
    if not os.path.exists(eventsfile):
        raise IOError, "%s does not exist" % eventsfile
    
    try:
        nevents  = int(nevents)
    except:
        raise ValueError, "Cannot convert %s to integer" % nevents
    
    if not isinstance(pixelpositionsfile, basestring):
        raise ValueError, "%s is not a str" % pixelpositionsfile
    import os
    if not os.path.exists(pixelpositionsfile):
        raise IOError, "%s does not exist" % pixelpositionsfile
    
    try:
        npixels  = int(npixels)
    except:
        raise ValueError, "Cannot convert %s to integer" % npixels

    # for details of units used
    # see Event2QE.h
    mod2sample = mod2sample/pyre.units.length.meter
    Ei = Ei/pyre.units.energy.meV
    Qmin, Qmax, dQ = Qaxis
    Emin, Emax, dE = Eaxis
    tofUnit = tofUnit/pyre.units.time.second
    toffset = tofUnit/pyre.units.time.microsecond
    tofmax = tofmax/pyre.units.time.microsecond
    args = [
        eventsfile,
        nevents,
        Qmin, Qmax, dQ,
        Ebegin, Eend, dE,
        Ei, 
        pixelpositionsfile,
        npixels,
        tofUnit,
        mod2sample,
        toffset,
        tofmax
        ]
    cmd = 'events2iqe ' + ' '.join([str(a) for a in args])
    print cmd
    if os.system(cmd):
        raise RuntimeError, "%s failed" % cmd
    return


from event_utils import readEvents as readevents


# version
__id__ = "$Id$"

# End of file 
