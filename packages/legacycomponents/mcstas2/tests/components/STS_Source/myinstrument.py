import mcvine, mcvine.components as mcomps

def instrument(moderator_datafile=None):
    instrument = mcvine.instrument()

    source = mcomps.sources.STS_Source(
        name='moderator',
        Emin=3, Emax=82.,
        dist=2.5,
        filename=moderator_datafile,
        focus_xw=0.03, focus_yh=0.03,
        xwidth=0.03, yheight=0.03,
    )
    instrument.append(source, position=(0.0, 0.0, 0.0), orientation=(0, 0, 0))

    L_monitor = mcomps.monitors.L_monitor(
        name='L_monitor', Lmax=5, Lmin=1, filename="I_lambda.dat",
        nchan=100, xwidth=0.03, yheight=0.03)
    instrument.append(L_monitor, position=(0.0, 0.0, 2.5), orientation=(0, 0, 0))

    tof_monitor = mcomps.monitors.TOF_monitor2(
        name='tof_monitor',
        xmin=-0.03, xmax=0.03,
        ymin=-0.03, ymax=0.03,
        tmin=0., tmax=0.015,
        nchan=100,
        filename = 'I_tof.dat'
    )
    instrument.append(tof_monitor, position=(0.0, 0.0, 10.), orientation=(0, 0, 0))
    return instrument
