# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#


def populate_Ei_data(sim_out, nxs):
    import h5py
    f = h5py.File(nxs, 'a')
    entry = f['entry']
    from mcvine.instruments.ARCS.nxs.raw import populateEiData
    populateEiData(entry, sim_out)
    return


def populate_monitor_data(sim_out, nxs)
    import h5py
    f = h5py.File(nxs, 'a')
    entry = f['entry']
    from mcvine.instruments.ARCS.nxs.raw import populateMonitors
    populateMonitors(entry, sim_out)
    return

