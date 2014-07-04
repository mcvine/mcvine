# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2008-2014  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
This module helps creating "raw" HYSPEC nexus file.
"""

def write(events, tofbinsize, path):
    """ write neutron events into a HYSPEC nexus file
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


def populateMetadata(entry, sim_out, sample, detector):
    """populate metadata needed for correct reduction by mantid
    This includes 
      * EnergyRequest
      * msd: LMS
      * s1: detector vessel angle
      * s2: sample angle
      
    entry: nexus "entry"
    sim_out: moderator2sample HYSPEC simulation output directory
    sample: sample angle (degrees)
    detector: detector angle (degrees)

    Limitations:
    """
    # read props 
    props = os.path.join(sim_out, 'props.json')
    props = eval(open(props).read())
    # get values
    Ei = float(props['average energy'].split()[0])
    LMS = float(props['monochromator-sample distance'].split()[0])
    
    # set energy
    setEnergyRequest(entry, Ei)
    
    # set msd
    setDASlogsEntryValue(entry, 'msd', LMS*1000) # unit: mm
    
    # 
    setDASlogsEntryValue(entry, 's1', detector)
    setDASlogsEntryValue(entry, 's2', sample)
    return


def setDASlogsEntryValue(entry, name, value):
    daslogs = entry['DASlogs']
    ds = daslogs[name]
    ds['average_value'][0] \
        = ds['effective_value'][0] \
        = ds['maximum_value'][0] \
        = ds['minimum_value'][0] \
        = ds['value'][0] \
        = value
    # "EnergyRequest" does not have "requested_value"
    # other items (s1,s2, etc) have.
    if not 'request' in name.lower():
        ds['requested_value'][0] = value
    return


def setEnergyRequest(entry, Ei):
    """set energy request value into an ARCS nexus file
    
    entry: nexus "entry"
    Ei: unit meV
    
    caveat: the nexus template file should already have /entry/DASlogs/EnergyRequest which contains the appropriate sub-datasets with correct attributes.
    """
    setDASlogsEntryValue(entry, 'EnergyRequest', Ei)
    return


bank_id_offset = 1
pixelsperbank = 8 * 128
pixel_id_offset = (bank_id_offset-1)*pixelsperbank
nbanks = 20
npixels = nbanks * pixelsperbank
import os
from mcvine.deployment_info import mcvinedir
nxs_template = os.path.join(mcvinedir, 'share', 'mcvine', 'instruments', 'HYSPEC', 'hyspec-raw-events-template.nxs')
import numpy as np


# End of file 
