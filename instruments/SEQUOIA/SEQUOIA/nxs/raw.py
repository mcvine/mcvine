# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2008-2016  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
This module helps creating "raw" SEQUOIA nexus file.
"""

def write(events, tofbinsize, path):
    """ write neutron events into a SEQUOIA nexus file
    The events is a numpy array of "event" records. 
    An event record has three fields:
      * pixelID
      * tofChannelNo
      * p

    tofbinsize * tofChannelNo is the tof for the bin
    path is the output path
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
        be = entry['bank%s_events' % (bank+bank_id_offset)]
        be['event_id'] = bevts['pixelID'] + pixel_id_offset
        be['event_time_offset'] = np.array(bevts['tofChannelNo'], dtype='float32') * tofbinsize
        be['event_time_offset'].attrs['units'] = 'microsecond'
        be['event_weight'] = np.array(bevts['p'], dtype='float32')
        be['event_index'] = np.array([0, len(bevts)], dtype='uint64')
        be['event_time_zero'] = np.array([0, 1./60], dtype='float64')
        etz = be['event_time_zero']
        # hack
        etz_attrs['target'] = '/entry/instrument/bank%s/event_time_zero' % (bank+bank_id_offset)
        for k,v in etz_attrs.items(): etz.attrs[k] = v
        
        # XXX: should this be a float and the sum of all weights?
        # XXX: michael reuter said this is not really used
        be['total_counts'][0] = len(bevts)

        # bank directory
        b = entry['bank%s' % (bank+bank_id_offset)]
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


def populateEiData(entry, sim_out):
    """populate data related to Ei computation into an SEQUOIA nexus file.
    This includes the monitor data and DASlog/EnergyRequest
    
    entry: nexus "entry"
    sim_out: moderator2sample SEQUOIA simulation output directory
      it should contains monitor data files mon?-itof-focused.h5,
      where ? = 1 and 2, and ienergy.h5

    Limitations:
      monitor positions are now hard-coded as (from moderator)
      1: 11.831
      2: 18.5
      need to make sure it matches what mantid is using
    """
    # compute average Ei
    import histogram.hdf as hh, numpy as np
    ienergy_h5 = os.path.join(sim_out, 'ienergy.h5')
    ie = hh.load(ienergy_h5)
    Ei = (ie.energy * ie.I).sum() / ie.I.sum()
    #
    setEnergyRequest(entry, Ei)
    populateMonitors(entry, sim_out)
    return


def setEnergyRequest(entry, Ei):
    """set energy request value into an SEQUOIA nexus file
    
    entry: nexus "entry"
    Ei: unit meV
    
    caveat: the nexus template file should already have /entry/DASlogs/EnergyRequest which contains the appropriate sub-datasets with correct attributes.
    """
    daslogs = entry['DASlogs']
    er = daslogs['EnergyRequest']
    er['average_value'][0] \
        = er['maximum_value'][0] \
        = er['minimum_value'][0] \
        = er['value'][0] \
        = Ei
    return


def populateMonitors(entry, sim_out):
    """populate monitor data into an SEQUOIA nexus file
    
    entry: nexus "entry"
    sim_out: moderator2sample SEQUOIA simulation output directory
      it should contains monitor data files mon?-itof-focused.h5,
      where ? = 1 and 2

    Limitations:
      monitor positions are now hard-coded (see below)
    """
    import histogram.hdf as hh, numpy as np
    dists = [m1, m2]
    itofpaths = [
        os.path.join(sim_out, 'mon%s-itof-focused.h5' % i)
        for i in range(1,3)
        ]
    for i, (dist, itofpath) in enumerate(zip(dists, itofpaths)):
        # check entry
        mon_entry = entry['monitor%s' % (i+1)]
        # assert mon_entry['distance'][0] == dist - sample
        mon_entry['distance'][0] = dist - sample
        tof_entry = mon_entry['time_of_flight']
        assert tof_entry[0] == 0. and tof_entry[1] == 1.
        # data
        hist = hh.load(itofpath)
        tofaxis = hist.axisFromName('tof'); tofaxis.changeUnit('microsecond')
        bb = tofaxis.binBoundaries().asNumarray()
        tofmin = bb[0]; tofmax = bb[-1]
        # XXX Michael Reuter said that float array is OK.
        # change array to double
        N = len(mon_entry['data'])
        del mon_entry['data']
        mon_entry['data'] = np.zeros(N, dtype="double")
        # set attributes
        mon_entry['data'].attrs['signal'] = 1
        mon_entry['data'].attrs['axes'] = 'time_of_flight'
        # set data
        mon_entry['data'][int(tofmin): int(tofmax)] = hist.I
        continue
    return

recorder = 19.9
sample = recorder + 0.1254
m1 = 18.26
m2 = 29.0032


bank_id_offset = 38
pixelsperbank = 8 * 128
pixel_id_offset = (bank_id_offset-1)*pixelsperbank
nbanks = 37+39+37
npixels = nbanks * pixelsperbank
import os
from mcvine import resources as res
nxs_template = os.path.join(
    res.instrument('SEQUOIA'), 'resources',
    'sequoia-raw-events-template.nxs')
import numpy as np


# End of file 
