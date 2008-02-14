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


def readevents( filename ):
    import numpy as N
    datatype = N.dtype( [ ('pixelID', N.uint32), ('tofchannel', N.uint32), ('n', N.double) ] )
    s = open(filename).read()
    events = N.fromstring( s, dtype = datatype )
    print len(events)
    print events[0]
    return events



# version
__id__ = "$Id$"

# End of file 
