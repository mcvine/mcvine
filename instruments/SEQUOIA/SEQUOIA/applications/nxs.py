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
def reduce(
        nxsfile, qaxis, outfile, use_ei_guess=False,
        ei_guess=None, eaxis=None):
    from mantid.simpleapi import DgsReduction, SofQW3, SaveNexus, SaveNXSPE, LoadInstrument, Load, MoveInstrumentComponent

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

    DgsReduction(
        SampleInputFile=nxsfile,
        IncidentEnergyGuess=ei_guess,
        UseIncidentEnergyGuess=use_ei_guess,
        OutputWorkspace='reduced',
        EnergyTransferRange=eaxis,
    )
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
