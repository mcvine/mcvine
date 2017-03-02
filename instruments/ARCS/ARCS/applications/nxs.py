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


def reduce(nxsfile, qaxis, outfile, use_ei_guess=False, ei_guess=None, eaxis=None, tof2E=True, ibnorm='ByCurrent'):
    from mantid.simpleapi import DgsReduction, SofQW3, SaveNexus, Load, GetEiT0atSNS
    if tof2E == 'guess':
        # XXX: this is a simple guess. all raw data files seem to have root "entry"
        cmd = 'h5ls %s' % nxsfile
        import subprocess as sp, shlex
        o = sp.check_output(shlex.split(cmd)).strip().split()[0]
        tof2E = o == 'entry'
    if tof2E:
        if use_ei_guess:
            DgsReduction(
                SampleInputFile=nxsfile,
                IncidentEnergyGuess=ei_guess,
                UseIncidentEnergyGuess=use_ei_guess,
                OutputWorkspace='reduced',
                EnergyTransferRange=eaxis,
                IncidentBeamNormalisation=ibnorm,
                )
        else:
            ws = Load(nxsfile)
            Eguess=ws.getRun()['EnergyRequest'].getStatistics().mean
            try:
                Efixed,T0=GetEiT0atSNS(ws,Eguess)
            except:
                import warnings
                warnings.warn("Failed to determine Ei from monitors. Use EnergyRequest log %s" % Eguess)
                Efixed,T0 = Eguess, 0
            
            DgsReduction(
                SampleInputFile=nxsfile,
                IncidentEnergyGuess=Efixed,
                UseIncidentEnergyGuess=True,
                TimeZeroGuess = T0,
                OutputWorkspace='reduced',
                EnergyTransferRange=eaxis,
                IncidentBeamNormalisation=ibnorm,
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
