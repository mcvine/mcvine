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


from .event_utils import readEvents as readevents


# version
__id__ = "$Id$"

# End of file 
