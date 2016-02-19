#!/usr/bin/env python


__doc__ = """
converte events.dat to nexus file.

events.dat are generated by mcvine simulation that sends scattereted neutrons
to ARCS detector system.

"""

def run(eventfile, nxsfile, tofbinsize=0.1, type="processed", Ei = None):
    """tofbinsize: in microsecond
    type: processed or raw. processed is obsolete but kept for backward compatibility
    Ei: nominal incident energy in meV    
    """
    print (eventfile, nxsfile)
    from mccomponents.detector.event_utils import readEvents
    events = readEvents(eventfile)
    
    prefix = 'mcvine.instruments.ARCS.nxs'
    mod = '%s.%s' % (prefix, type)
    mod = __import__(mod, fromlist = [''])
    mod.write(events, tofbinsize, nxsfile, Ei=Ei)
    return
