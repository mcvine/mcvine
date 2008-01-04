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


def he3tubeKernel( *args, **kwds ):
    from register_He3TubeKernel import He3TubeKernel
    return He3TubeKernel(*args, **kwds )


def he3tube( *args, **kwds ):
    from register_He3Tube import He3Tube
    return He3Tube(*args, **kwds)


def pixel( *args, **kwds):
    from register_He3Tube import Pixel
    return Pixel(*args, **kwds)


def detectorSystem( *args, **kwds ):
    from register_DetectorSystem import DetectorSystem
    return DetectorSystem( *args, **kwds )


def eventModeMCA( *args, **kwds ):
    from register_EventModeMCA import EventModeMCA
    return EventModeMCA( *args, **kwds )


# version
__id__ = "$Id$"

# End of file 
