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



def detectorcomponent( name, instrumentxml, coordinate_system, tofparams, outfilename ):
    import mccomposite.register_Copy
    import mccomposite.register_HollowCylinder
    
    from instrument.nixml import parse_file
    instrument = parse_file( instrumentxml )
    
    import instrument.geometers as ig
    instrument.geometer.changeRequestCoordinateSystem(
        ig.coordinateSystem( coordinate_system ) )
        
    from mccomponents.detector.utils import \
         getDetectorHierarchyDimensions, assignLocalGeometers
    assignLocalGeometers( instrument, coordinate_system = coordinate_system )
        
    detectorSystem = instrument.getDetectorSystem()

    detectorSystem.tofparams = tofparams
    dims = getDetectorHierarchyDimensions( instrument )
    dims = [ dim for name, dim in dims ]

    
    mca = eventModeMCA(  outfilename, dims )
    detectorSystem.mca = mca

    import mccomponents.homogeneous_scatterer as mh
    cds = mh.scattererEngine( detectorSystem, coordinate_system = coordinate_system )

    instrument.geometer = instrument.global_geometer

    cds.name = name
    return cds


import units

def he3tube_withpixels(
    radius = units.length.inch/2, height = units.length.meter,
    npixels = 128, direction = 'z', id = 0, pressure = 10*units.pressure.atm,
    mcweights = (0.9,0,0.1),
    ):

    import mccomposite.geometry.primitives as primitives
    cylinder = primitives.cylinder( radius, height )
    import mccomposite.geometry.operations as operations
    if direction == 'x':
        shape = operations.rotate( cylinder, (0,90,0) )
    elif direction == 'y':
        shape = operations.rotate( cylinder, (-90,0,0) )
    elif direction == 'z':
        shape = cylinder
    else:
        raise ValueError, "direction must be x, y, or z: %s" % direction
    
    ret = he3tube(
        cylinder, id = id,
        pressure = pressure,
        mcweights \
        = mcweights
        )

    import numpy as N
    start = -(npixels-1)/2./npixels*height
    step = height/npixels
    displacements = N.array([start + step*i for i in range(npixels)])

    positions = N.zeros( (npixels, 3) ) * units.length.meter
    ind = {'x': 0,
           'y': 1,
           'z': 2} [ direction ]
    positions[:, ind] = displacements

    for i in range(npixels):
        pxl = pixel( id = i )
        ret.addElement(pxl, positions[i] )
        continue

    return ret


def pack( *args, **kwds ):
    from register_DetectorPack import DetectorPack
    return DetectorPack(*args, **kwds)


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


def _register_all():
    import register_CompositeDetector
    import register_DetectorPack
    import register_DetectorSystem
    import register_EventModeMCA
    import register_He3Tube
    import register_He3TubeKernel
    return

_register_all()


# version
__id__ = "$Id$"

# End of file 
