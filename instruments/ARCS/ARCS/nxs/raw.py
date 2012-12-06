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
This module helps creating "raw" ARCS nexus file.
"""

def write(events, tofbinsize, path):
    import shutil, sys
    shutil.copyfile(nxs_template, path)
    import time; time.sleep(0.5)
    import h5py
    f = h5py.File(path, 'a')
    entry = f['entry']

    # XXX: hack
    etz_attrs = {
        'units': 'second',
        'offset': '2012-08-23T11:23:53.833508666-04:00',
        'offset_seconds': 714583433,
        'offset_nanoseconds': 833508666,
        }
    
    for bank in range(nbanks):
        # print bank
        sys.stdout.write('.')
        # bank events
        pixelidstart = bank * pixelsperbank
        pixelidend = pixelidstart + pixelsperbank
        bevts = events[(events['pixelID']<pixelidend) * (events['pixelID']>=pixelidstart)]
        if not bevts.size:
            # fake events. mantid cannot handle empty events
            bevts = events[0:1].copy()
            evt = bevts[0]
            evt['pixelID'] = pixelidstart
            evt['tofChannelNo'] = 0
            evt['p'] = 0
        
        # bank events directory 
        be = entry['bank%s_events' % (bank+1)]
        be['event_id'] = bevts['pixelID']
        be['event_time_offset'] = np.array(bevts['tofChannelNo'], dtype='float32') * tofbinsize
        be['event_time_offset'].attrs['units'] = 'microsecond'
        be['event_weight'] = np.array(bevts['p'], dtype='float32')
        be['event_index'] = np.array([0, len(bevts)], dtype='uint64')
        be['event_time_zero'] = np.array([0, 1./60], dtype='float64')
        etz = be['event_time_zero']
        # hack
        etz_attrs['target'] = '/entry/instrument/bank%s/event_time_zero' % (bank+1)
        for k,v in etz_attrs.items(): etz.attrs[k] = v
        
        # XXX: should this be a float and the sum of all weights?
        # XXX: michael reuter said this is not really used
        # be['total_counts'][0] = len(bevts)

        # bank directory
        b = entry['bank%s' % (bank+1)]
        # XXX: should this be float array?
        # XXX: michael reuter said this is not really used
        # compute histogram
        # h, edges = np.histogram(bevts['pixelID'], pixelsperbank, range=(pixelidstart-0.5, pixelidend-0.5)) # weights = ?
        # h.shape = 8, 128
        # b['data_x_y'][:] = np.array(h, dtype='uint32')
        
        continue

    # XXX: should it be a float?
    # entry['total_counts'][0] = len(events)

    #
    f.close()
    #
    sys.stdout.write('\n')
    return


nbanks = 38+39+38
pixelsperbank = 8 * 128
npixels = nbanks * pixelsperbank
import os
from mcvine.deployment_info import mcvinedir
nxs_template = os.path.join(mcvinedir, 'share', 'mcvine', 'instruments', 'ARCS', 'arcs-raw-events-template.nxs')
import numpy as np


# End of file 
