# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#


def populate_Ei_data(sim_out, nxs):
    import h5py
    f = h5py.File(nxs, 'a')
    entry = f['entry']
    from mcvine.instruments.SEQUOIA.nxs.raw import populateEiData
    populateEiData(entry, sim_out)
    return


def populate_monitor_data(sim_out, nxs):
    import h5py
    f = h5py.File(nxs, 'a')
    entry = f['entry']
    from mcvine.instruments.SEQUOIA.nxs.raw import populateMonitors
    populateMonitors(entry, sim_out)
    return


# this is almost the same as the ARCS version
# this is different from the previous sequoia-reduce-nxs-using-mantid
# since the nxspe write out is not implemented here.
# NXSPE may not be necessary because we can just use the code
# in mcvine workflow single crystal reduce scripts and skip nxspe
def reduce(nxsfile, qaxis, outfile, use_ei_guess=False, ei_guess=None, eaxis=None, tof2E=True, ibnorm='ByCurrent'):
    from mantid.simpleapi import DgsReduction, SofQW3, SaveNexus, LoadInstrument, Load, MoveInstrumentComponent, MaskBTP
    
    if tof2E == 'guess':
        # XXX: this is a simple guess. all raw data files seem to have root "entry"
        cmd = 'h5ls %s' % nxsfile
        import subprocess as sp, shlex
        o = sp.check_output(shlex.split(cmd)).strip().split()[0]
        tof2E = o == 'entry'
    
    if tof2E:
        ws = Load(nxsfile)
        # mask packs around beam
        MaskBTP(ws, Bank="98-102")
        if use_ei_guess:
            DgsReduction(
                SampleInputWorkspace=ws,
                IncidentEnergyGuess=ei_guess,
                UseIncidentEnergyGuess=use_ei_guess,
                OutputWorkspace='reduced',
                EnergyTransferRange=eaxis,
                IncidentBeamNormalisation=ibnorm,
                )
        else:
            Eguess=ws.getRun()['EnergyRequest'].getStatistics().mean
            try:
                Efixed,T0=GetEiT0atSNS(ws,Eguess)
            except:
                import warnings
                warnings.warn("Failed to determine Ei from monitors. Use EnergyRequest log %s" % Eguess)
                Efixed,T0 = Eguess, 0
            
            DgsReduction(
                SampleInputWorkspace=ws,
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


# do we still need MoveInstrumentComponent?
"""
    # load workspace from input nexus file
    workspace = Load(nxsfile)
    
    # XXX: the following line seems to cause trouble. probably a bug in Mantid?
    # LoadInstrument(workspace, idfpath) 
    
    # change moderator position
    # mantid: z=-20.0114
    # mcvine: z=-20.0254
    # need shift: z=-0.014
    MoveInstrumentComponent(workspace, "moderator", -1, 0, 0, -0.014, True) # workspace, component, detector, x,y,z, relative
    # MoveInstrumentComponent(workspace, "moderator", -1, 0, 0, -20.0254, False) # workspace, component, detector, x,y,z, relative

"""
