# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import numpy as np

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
    from mantid.simpleapi import DgsReduction, SofQW3, SaveNexus, LoadInstrument, Load, MoveInstrumentComponent, \
        MaskBTP, ConvertToMD, BinMD, ConvertMDHistoToMatrixWorkspace, GetEiT0atSNS, GetEi
    from mantid import mtd
    
    if tof2E == 'guess':
        # XXX: this is a simple guess. all raw data files seem to have root "entry"
        cmd = 'h5ls %s' % nxsfile
        import subprocess as sp, shlex
        o = sp.check_output(shlex.split(cmd)).strip().split()[0]
        tof2E = o == 'entry'
    
    if tof2E:
        ws, mons = Load(nxsfile, LoadMonitors=True)
        # mask packs around beam
        MaskBTP(ws, Bank="98-102")
        if not use_ei_guess:
            Eguess=ws.getRun()['EnergyRequest'].getStatistics().mean
            try:
                Efixed,_p,_i,T0=GetEi(InputWorkspace=mons,Monitor1Spec=1,Monitor2Spec=2,EnergyEstimate=Eguess,FixEi=False)
            except:
                import warnings
                warnings.warn("Failed to determine Ei from monitors. Use EnergyRequest log %s" % Eguess)
                Efixed,T0 = Eguess, 0
        else:
            Efixed, T0 = ei_guess, 0

        DgsReduction(
            SampleInputWorkspace=ws,
            IncidentEnergyGuess=Efixed,
            UseIncidentEnergyGuess=True,
            TimeZeroGuess = T0,
            OutputWorkspace='reduced',
            EnergyTransferRange=eaxis,
            IncidentBeamNormalisation=ibnorm,
            )
        reduced = mtd['reduced']
    else: 
        reduced = Load(nxsfile)

    # if eaxis is not specified, use the data in reduced workspace
    if eaxis is None:
        Edim = reduced.getXDimension()
        emin = Edim.getMinimum()
        emax = Edim.getMaximum()
        de = Edim.getX(1) - Edim.getX(0)
        eaxis = emin, emax, de
        
    qmin, dq, qmax = qaxis; nq = int(round((qmax-qmin)/dq))
    emin, de, emax = eaxis; ne = int(round((emax-emin)/de))
    md = ConvertToMD(
        InputWorkspace='reduced',
        QDimensions='|Q|',
        dEAnalysisMode='Direct',
        MinValues="%s,%s" % (qmin, emin),
        MaxValues="%s,%s" % (qmax, emax),
        SplitInto="%s,%s" % (nq, ne),
        )
    binned = BinMD(
        InputWorkspace=md,
        AxisAligned=1,
        AlignedDim0="|Q|,%s,%s,%s" % (qmin, qmax, nq),
        AlignedDim1="DeltaE,%s,%s,%s" % (emin, emax, ne),
        )
    iqw = ConvertMDHistoToMatrixWorkspace(
        InputWorkspace='binned',
        OutputWorkspace='iqw',
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
