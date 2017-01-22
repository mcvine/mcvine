# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

def populate_metadata(sim_out, nxs, sample, detector):
    import h5py
    f = h5py.File(nxs, 'a')
    entry = f['entry']
    from mcvine.instruments.HYSPEC.nxs.raw import populateMetadata
    populateMetadata(entry, sim_out, sample, detector)
    return

# End of file
