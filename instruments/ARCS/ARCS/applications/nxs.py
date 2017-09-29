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


def reduce(nxsfile, qaxis, outfile, use_ei_guess=False, ei_guess=None, eaxis=None, tof2E=True, ibnorm='ByCurrent', t0_guess=None):
    from mantid.simpleapi import DgsReduction, LoadInstrument, Load, MoveInstrumentComponent, GetEiT0atSNS, GetEi
    from mantid import mtd

    if tof2E == 'guess':
        # XXX: this is a simple guess. all raw data files seem to have root "entry"
        cmd = 'h5ls %s' % nxsfile
        import subprocess as sp, shlex
        o = sp.check_output(shlex.split(cmd)).strip().split()[0]
        tof2E = o == 'entry'

    if tof2E:
        ws, mons = Load(nxsfile, LoadMonitors=True)
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

    getSqeHistogramFromMantidWS(reduced, outfile, qaxis, eaxis)
    return


def getSqeHistogramFromMantidWS(reduced, outfile, qaxis=None, eaxis=None):
    from mantid import simpleapi as msa
    # if eaxis is not specified, use the data in reduced workspace
    if eaxis is None:
        Edim = reduced.getXDimension()
        emin = Edim.getMinimum()
        emax = Edim.getMaximum()
        de = Edim.getX(1) - Edim.getX(0)
        eaxis = emin, de, emax
        
    qmin, dq, qmax = qaxis; nq = int(round((qmax-qmin)/dq))
    emin, de, emax = eaxis; ne = int(round((emax-emin)/de))
    md = msa.ConvertToMD(
        InputWorkspace=reduced,
        QDimensions='|Q|',
        dEAnalysisMode='Direct',
        MinValues="%s,%s" % (qmin, emin),
        MaxValues="%s,%s" % (qmax, emax),
        SplitInto="%s,%s" % (nq, ne),
        )
    binned = msa.BinMD(
        InputWorkspace=md,
        AxisAligned=1,
        AlignedDim0="|Q|,%s,%s,%s" % (qmin, qmax, nq),
        AlignedDim1="DeltaE,%s,%s,%s" % (emin, emax, ne),
        )
    # convert to histogram
    import histogram as H, histogram.hdf as hh
    data=binned.getSignalArray().copy()
    err2=binned.getErrorSquaredArray().copy()
    nev=binned.getNumEventsArray()
    data/=nev
    err2/=(nev*nev)
    import numpy as np
    qaxis = H.axis('Q', boundaries=np.arange(qmin, qmax+dq/2., dq), unit='1./angstrom')
    eaxis = H.axis('E', boundaries=np.arange(emin, emax+de/2., de), unit='meV')
    hist = H.histogram('IQE', (qaxis, eaxis), data=data, errors=err2)
    if outfile.endswith('.nxs'):
        import warnings
        warnings.warn("reduce function no longer writes iqe.nxs nexus file. it only writes iqe.h5 histogram file")
        outfile = outfile[:-4] + '.h5'
    hh.dump(hist, outfile)
    return
