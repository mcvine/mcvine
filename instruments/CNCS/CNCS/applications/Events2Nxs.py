#!/usr/bin/env python
#
#   Jiao Lin
#


"""
This module helps creating "processed" nexus file.

"processed" nexus file is created by mantid. it is
actually a mantid workspace file.

This was used in the first attempt of creating CNCS event
nexus file for simulated events. 
"""

from mcvine import resources
import os


nbanks = 50
nmonitors = 0
nxs_template = os.path.join(
    resources.instrument('CNCS'), 'nxs', 'cncs-processed-template.nxs')


def run(eventfile, nxsfile, tofbinsize=0.1, type=None, Ei=None):
    """tofbinsize: in microsecond
    """
    assert type=='processed', "Unsupported type %r" % type
    import warnings
    warnings.warn("Ei=%s was not utilized" % Ei)
    print (eventfile, nxsfile)
    # read events
    from mccomponents.detector.event_utils import readEvents
    events = readEvents(eventfile)
    # write nxs
    write(events, tofbinsize, nxsfile)
    return


def write(events, tofbinsize, nxsfile):
    # tofbinsize must be in the unit of microsecond
    data = convert(events)
    data['tofbinsize'] = tofbinsize
    _write(nxsfile, **data)
    return


npixels = nbanks*8*128
def convert(events):
    """convert simulated events to data to be written
    to "processed" nexus file
    """
    events.sort(order='pixelID')
    pixelids = events['pixelID'] + 1 + nmonitors # !!!!! spectrum number for pixel #0 is 1+nmonitors. You can see this by Right click nxs file, show detectors.
    hist, bin_edges = np.histogram(
        pixelids, 
        bins=np.arange(-0.5, npixels+1.5), 
        )
    indices = np.cumsum(hist)
    
    nevents = len(events)
    pulse_time = np.zeros(nevents)
    
    tof = events['tofChannelNo'] # XXX: tof unit?
    weights = events['p']
    
    return {
        'indices': indices,
        'pulse_time': pulse_time,
        'tof': tof,
        'weights': weights,
        }


def _write(
    path,
    indices=None, pulse_time=None,
    tof=None, tofbinsize=None,
    weights=None):
    """write "processed" nexus file given relevant data
    """
    import shutil
    shutil.copyfile(nxs_template, path)
    import time; time.sleep(0.5)
    import h5py
    f = h5py.File(path, 'a')
    e = f['mantid_workspace_1']['event_workspace']
    e['indices'] = indices
    e['pulsetime'] = pulse_time
    tofarr = e['tof'] = np.array(tof, dtype="double") * tofbinsize
    e['weight'] = np.array(weights, dtype='float32')
    e['error_squared'] = np.array(weights, dtype='float32')**2
    e['axis1'][:] = np.min(tofarr)-100, np.max(tofarr)+100
    f.close()
    return


import numpy as np


# End of file 
