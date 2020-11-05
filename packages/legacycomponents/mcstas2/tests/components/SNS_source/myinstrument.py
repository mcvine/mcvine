import mcvine, mcvine.components as mcomps
instrument = mcvine.instrument()

source = mcomps.sources.SNS_source(
    name='source',
    S_filename="source_sct521_bu_17_1.dat",
    width=0.1, height = 0.12,
    dist=2.5,
    xw=0.1, yh=0.12,
    Emin = 0.0, Emax = 200.0
)
instrument.append(source, position=(0.0, 0.0, 0.0), orientation=(0, 0, 0))

L_monitor = mcomps.monitors.L_monitor(
    name='L_monitor', Lmax=5, Lmin=0, filename="I_lambda.dat",
    nchan=100, xwidth=0.1, yheight=0.1)
instrument.append(L_monitor, position=(0.0, 0.0, 2.5), orientation=(0, 0, 0))

tof_monitor = mcomps.monitors.TOF_monitor2(
    name='tof_monitor',
    xmin=-0.05, xmax=0.05,
    ymin=-0.05, ymax=0.05,
    tmin=0., tmax=0.01,
    nchan=100,
    filename = 'I_tof.dat'
)
instrument.append(tof_monitor, position=(0.0, 0.0, 10.), orientation=(0, 0, 0))
