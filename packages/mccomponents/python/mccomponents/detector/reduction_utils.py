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


import journal
debug = journal.debug("mcvine.detector.reduction_utils")


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
    intensityfile,
    pixelpositionsfile, solidanglesfile, 
    npixels,
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
    pixelpositionsfile:  filename for pixel positions. position unit:meter
    solidanglesfile: filename for pixel solid angles. solid angle unit: sr
    npixels:
    mod2sample: moderator to sample distance 
    Ei: incident energy
    Qaxis, Eaxis: (min, max, step) of Q and E
    '''
    if not isinstance(eventsfile, str):
        raise ValueError("%s is not a str" % eventsfile)
    import os
    if not os.path.exists(eventsfile):
        raise IOError("%s does not exist" % eventsfile)
    
    try:
        nevents  = int(nevents)
    except:
        raise ValueError("Cannot convert %s to integer" % nevents)

    if not isinstance(intensityfile, str):
        raise ValueError("%s is not a str" % intensityfile)
    
    if not isinstance(pixelpositionsfile, str):
        raise ValueError("%s is not a str" % pixelpositionsfile)
    import os
    if not os.path.exists(pixelpositionsfile):
        raise IOError("%s does not exist" % pixelpositionsfile)
    
    if not isinstance(solidanglesfile, str):
        raise ValueError("%s is not a str" % solidanglesfile)
    if not os.path.exists(solidanglesfile):
        raise IOError("%s does not exist" % solidanglesfile)

    try:
        npixels  = int(npixels)
    except:
        raise ValueError("Cannot convert %s to integer" % npixels)

    # for details of units used
    # see Event2QE.h
    mod2sample = mod2sample/pyre.units.length.meter
    Ei = Ei/pyre.units.energy.meV
    Qmin, Qmax, dQ = Qaxis
    Emin, Emax, dE = Eaxis
    tofUnit = tofUnit/pyre.units.time.second
    toffset = toffset/pyre.units.time.microsecond
    tofmax = tofmax/pyre.units.time.microsecond
    args = [
        eventsfile,
        nevents,
        intensityfile,
        Qmin, Qmax, dQ,
        Emin, Emax, dE,
        Ei, 
        pixelpositionsfile,
        solidanglesfile,
        npixels,
        tofUnit,
        mod2sample,
        toffset,
        tofmax
        ]
    cmd = 'events2iqe ' + ' '.join([str(a) for a in args])
    debug.log("running command %s" % cmd)
    import subprocess
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.wait():
        raise RuntimeError("%s failed" % cmd)
    nQ, nE = eval(out.strip().splitlines()[-1])

    import numpy
    i = numpy.fromfile(intensityfile, numpy.double)
    i.shape = nQ, nE
    from histogram import histogram, axis, arange
    Qaxis = axis(
        'Q',
        boundaries = arange(Qmin, Qmin+dQ*nQ+dQ/2, dQ), 
        unit = '1./angstrom',
        )
    Eaxis = axis(
        'E',
        boundaries = arange(Emin, Emin+dE*nE+dE/2, dE), 
        unit = 'meV',
        )
    iqe = histogram('IQE', [Qaxis, Eaxis], data = i)
    return iqe


from .event_utils import readEvents as readevents


# version
__id__ = "$Id$"

# End of file 
