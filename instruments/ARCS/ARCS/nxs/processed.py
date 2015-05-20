# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2008-2012  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
This module helps creating "processed" ARCS nexus file.

"processed" ARCS nexus file is created by mantid. it is
actually a mantid workspace file.

This was used in the first attempt of creating ARCS event
nexus file for simulated events. 
Since mantid has not yet immplmented data loader (Oct 2012)
that can load "real" ARCS nexus event file, we have to 
create "processed" ARCS nexus file.
It proved the concept of loading simulated ARCS data into
mantid GUI, and we were able to reduce the simulated
data to I(Q,E) with expected results.
"""

# XXX: Ei option not supported yet
def write(events, tofbinsize, nxsfile, Ei=None):
    # tofbinsize must be in the unit of microsecond
    data = convert(events)
    data['tofbinsize'] = tofbinsize
    _write(nxsfile, **data)
    return


npixels = (38+39+38) * 8 * 128
def convert(events):
    """convert simulated events to data to be written
    to "processed" ARCS nexus file
    """
    events.sort(order='pixelID')
    pixelids = events['pixelID']
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


import os
from mcvine import resources
nxs_template = os.path.join(
    resources.instrument('ARCS'), 'resources', 'arcs-events-template.nxs')
def _write(
    path,
    indices=None, pulse_time=None,
    tof=None, tofbinsize=None,
    weights=None):
    """write "processed" ARCS nexus file given relevant data
    """
    import shutil
    shutil.copyfile(nxs_template, path)
    import time; time.sleep(0.5)
    import h5py
    f = h5py.File(path, 'a')
    e = f['mantid_workspace_1']['event_workspace']
    e['indices'] = indices
    e['pulsetime'] = pulse_time
    e['tof'] = np.array(tof, dtype="double") * tofbinsize
    e['weights'] = weights
    f.close()
    return


import numpy as np


# End of file 
