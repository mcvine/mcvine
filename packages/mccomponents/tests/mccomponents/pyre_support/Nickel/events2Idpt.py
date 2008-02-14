#!/usr/bin/env python

from mccomponents.detector.reduction_utils import events2Ipixtof


def events2Idpt( events, instrument, tofparams ):
    from mccomponents.detector.utils import \
         getDetectorHierarchyDimensions
    dims = getDetectorHierarchyDimensions( instrument )
    # 1st attempt to create axes
    from histogram import histogram, axis, arange
    axes = [ axis('%sID' % name.lower(), range(n)) for name, n in dims ]

    # the first level of detectors (tubes, packs, or others) need
    # special attention. ids of that level could be not continuous.
    detectorSystem = instrument.getDetectorSystem()
    assert len(detectorSystem.elements()) == dims[0][1]
    ids = [ element.id() for element in detectorSystem.elements() ]
    axes[0] = axis( axes[0].name(), ids )

    detaxes = axes

    #tof axis
    tmin, tmax, tstep = tofparams
    tofaxis = axis( 'tof', boundaries = arange( tmin, tmax+tstep/10., tstep ), unit = 'second' )

    #all axes
    axes = detaxes + [tofaxis]

    #histogram
    hist = histogram( 'Idpt', axes )

    #get the numpy array which will accept events
    npixels = hist.size()/tofaxis.size()
    Ipixtof = hist.data().storage().asNumarray()
    Ipixtof.shape = npixels, -1
    events2Ipixtof( events, Ipixtof )

    return hist


def main():
    from sim_params import instrument, tofparams, eventsdat, Idpt_filename as filename
    
    from mccomponents.detector.reduction_utils import readevents
    events = readevents( eventsdat )

    Idpt = events2Idpt( events, instrument, tofparams )
    
    #save to file
    import os
    if os.path.exists(filename): os.remove( filename )
    import histogram.hdf as hh
    hh.dump( Idpt, filename, '/', 'c' )
    return


if __name__== '__main__': main()
