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


def events2IQE(events, pixelpositions, L1, vi, Ei=None):
    '''
    direct geometery inelastic neutron scattering reduction
    
    vf = r(pixel) / (t-t1)

    r(pixel): distance from smaple to pixel
    t: tof
    t1: time from source to sample
    
    E = Ei - Ef
    Q = ki - kf

    vi = (0, 0, vi)

    t1 = L1 / vi

    events: numpy array of events
    pixelpositions: numpy array of pixel positions
    '''
    

    return


from event_utils import readEvents as readevents


# version
__id__ = "$Id$"

# End of file 
