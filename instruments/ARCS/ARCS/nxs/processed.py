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

def write(events, nxsfile):
    data = convert(events)
    _write(nxsfile, *data)
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
    
    return indices, pulse_time, tof, weights


import os
from mcvine.deployment_info import mcvinedir
nxs_template = os.path.join(mcvinedir, 'share', 'mcvine', 'instruments', 'ARCS', 'arcs-events-template.nxs')
def _write(path, indices, pulse_time, tof, weights):
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
    e['tof'] = np.array(tof, dtype="double")
    e['weights'] = weights
    f.close()
    return


import numpy as np


# End of file 
