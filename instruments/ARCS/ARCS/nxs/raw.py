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

DASlogs: 
 * EnergyRequest
   * average_value
   * effective_value
   * maximum_value
   * minimum_value
   * value

It is kind of weird there are so many "value" items. But we will
just set all of them to the same value
"""

def write(events, tofbinsize, path, Ei=None):
    """ write neutron events into a ARCS nexus file

    Required parameters
        events: a numpy array of "event" records. 
          An event record has three fields:
            * pixelID
            * tofChannelNo
            * p

        tofbinsize * tofChannelNo is the tof for the bin

        path: the output path
    
    """

    # implementation details
    # -1. h5py is used for handling the file.
    # 0. make a new file by first copying a template file to a new file, and then adding new data
    # 1. events are splitted to banks and saved. for a bank, all events are in bank{i}_events
    # 2. any bank must have at least one event. if there are no events, we must assign fake ones
    
    import shutil, sys
    shutil.copyfile(nxs_template, path)
    import time; time.sleep(0.5)
    import h5py
    f = h5py.File(path, 'a')
    entry = f['entry']
    # Ei
    if Ei: setEnergyRequest(entry, Ei)

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
        
        # Rev1316, 2012, michael reuter said this is not really used
        # Oct 2013: michael reuter said this is used, and it should be the
        #   number of counts, not the sum of the probabilities
        be['total_counts'][0] = len(bevts)
        
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


def setEnergyRequest(entry, Ei):
    daslogs = entry['DASlogs']
    er = daslogs['EnergyRequest']
    er['average_value'][0] \
        = er['effective_value'][0] \
        = er['maximum_value'][0] \
        = er['minimum_value'][0] \
        = er['value'][0] \
        = Ei
    return


def populateMonitors(entry, sim_out):
    """populate monitor data into an ARCS nexus file
    
    entry: nexus "entry"
    sim_out: moderator2sample ARCS simulation output directory
      it should contains monitor data files mon?-itof-focused.h5,
      where ? = 1 and 2

    Limitations:
      monitor positions are now hard-coded as (from moderator)
      1: 11.831
      2: 18.5
    """
    import histogram.hdf as hh
    sample = 13.6
    dists = [11.831, 18.5]
    itofpaths = ['mon%s-itof-focused.h5' % i for i in range(1,3)]
    for i, (dist, itofpath) in enumerate(zip(dists, itofpaths)):
        # check entry
        mon_entry = entry['monitor%s' % (i+1)]
        assert mon_entry['distance'][0] == dist - sample
        tof_entry = mon_entry['time_of_flight']
        assert tof_entry[0] == 0. and tof_entry[1] == 1.
        # data
        hist = hh.load(itofpath)
        tofaxis = hist.axisFromName('tof'); tofaxis.changeUnit('microsecond')
        bb = tofaxis.binBoundaries().asNumarray()
        tofmin = bb[0]; tofmax = bb[-1]
        mon_entry['data'][int(tofmin): int(tofmax)] = hist.I
        continue
    return


nbanks = 38+39+38
pixelsperbank = 8 * 128
npixels = nbanks * pixelsperbank
import os
from mcvine.deployment_info import mcvinedir
nxs_template = os.path.join(mcvinedir, 'share', 'mcvine', 'instruments', 'ARCS', 'arcs-raw-events-template.nxs')
import numpy as np


# End of file 
