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


def populate_monitor_data(sim_out, nxs):
    import h5py
    f = h5py.File(nxs, 'a')
    entry = f['entry']
    from mcvine.instruments.ARCS.nxs.raw import populateMonitors
    populateMonitors(entry, sim_out)
    return


def reduce(nxsfile, qaxis, outfile, use_ei_guess=False, ei_guess=None, eaxis=None, tof2E=True):
    from mantid.simpleapi import DgsReduction, SofQW3, SaveNexus, Load
    if tof2E:
        if use_ei_guess:
            DgsReduction(
                SampleInputFile=nxsfile,
                IncidentEnergyGuess=ei_guess,
                UseIncidentEnergyGuess=use_ei_guess,
                OutputWorkspace='reduced',
                EnergyTransferRange=eaxis,
                )
        else:
            DgsReduction(
                SampleInputFile=nxsfile,
                OutputWorkspace='reduced',
                EnergyTransferRange=eaxis,
                )
    else: 
        reduced = Load(nxsfile)
    SofQW3(
        InputWorkspace='reduced',
        OutputWorkspace='iqw',
        QAxisBinning=qaxis,
        EMode='Direct',
        )
    SaveNexus(
        InputWorkspace='iqw',
        Filename = outfile,
        Title = 'iqw',
        )
    return
