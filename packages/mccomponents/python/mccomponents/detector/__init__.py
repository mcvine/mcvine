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



def detectorcomponent( name, instrumentxml, coordinate_system="McStas", tofparams=(0,0.02,1e-6), outfilename=None):
    import mccomposite.extensions.Copy
    from mccomposite.extensions import HollowCylinder, SphereShell
    import mccomponents.detector.optional_extensions.Detector
    
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

    from .DetectorSystemFromXml import DetectorSystemFromXml
    rt = DetectorSystemFromXml(cds, outfilename)
    rt.name = name
    return rt


def mergeEventFiles(files, out):
    "merge event data files into one output file"
    from .event_utils import mergeEventFiles
    return mergeEventFiles(files, out)


def normalizeEventFile(file, n):
    "normalize the event data file by the number n"
    from .event_utils import normalizeEventFile
    return normalizeEventFile(file, n)


from . import units

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
        raise ValueError("direction must be x, y, or z: %s" % direction)
    
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
    from .elements.DetectorPack import DetectorPack
    return DetectorPack(*args, **kwds)


def he3tubeKernel( *args, **kwds ):
    from .elements.He3TubeKernel import He3TubeKernel
    return He3TubeKernel(*args, **kwds )


def he3tube( *args, **kwds ):
    from .elements.He3Tube import He3Tube
    return He3Tube(*args, **kwds)


def pixel( *args, **kwds):
    from .elements.Pixel import Pixel
    return Pixel(*args, **kwds)


def detectorSystem( *args, **kwds ):
    from .elements.DetectorSystem import DetectorSystem
    return DetectorSystem( *args, **kwds )


def eventModeMCA( *args, **kwds ):
    from .elements.EventModeMCA import EventModeMCA
    return EventModeMCA( *args, **kwds )



def he3_absorption_coeff(energy, pressure):
    """pressure: unit: atm
    energy: unit: meV
    """
    from math import sqrt
    refAbsXS =  5333.0e-28/1.798
    N = pressure*101325 *2.414e20
    return refAbsXS * sqrt(81.81/energy) * N


def he3_transmission_percentage(energy, pressure, length):
    """
    pressure: atm
    energy: meV
    length: cm
    """
    length *= 0.01
    mu = he3_absorption_coeff(energy, pressure)
    from math import exp 
    return exp(-mu*length)



default_mc_weights_for_detector_scatterer = 0.9, 0.0, 0.1 # absorption, scattering, transmission


from . import ComputationEngineRendererExtension

def _import_bindings():
    try:
        from . import bindings
    except ImportError:
        import warnings
        warnings.warn('binding not imported')
    return

_import_bindings()


# version
__id__ = "$Id$"

# End of file 
