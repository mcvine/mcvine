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


# def events2IQE(events, pixelpositions, L1, 


from event_utils import readEvents as readevents


# version
__id__ = "$Id$"

# End of file 
