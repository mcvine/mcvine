import mcvine, mcvine.components as mcomps
instrument = mcvine.instrument()

arm = mcomps.optics.Arm(name='arm')
instrument.append(arm, position=(0.0, 0.0, 0.0), orientation=(0, 0, 0))

source = mcomps.sources.Source_simple(name='source', yh=0.015, dist=1, dE=0.2, xw=0.024, radius=0.015, E0=5)
instrument.append(source, position=(0.0, 0.0, 0.0), orientation=(0, 0, 0), relativeTo=arm)

collimator = mcomps.optics.Collimator_linear(name='collimator', ymax=0.03, divergence=coll_div, len=0.2, xmax=0.02, xmin=-0.02, ymin=-0.03)
instrument.append(collimator, position=(0.0, 0.0, 0.4), orientation=(0, 0, 0), relativeTo=arm)

target = mcomps.samples.V_sample(name='target', focus_r=0, yheight=0.015, target_z=1, target_x=0, target_y=0, xwidth=0.02, zthick=0.004, pack=1)
instrument.append(target, position=(0.0, 0.0, 1.0), orientation=(0, 0, 0), relativeTo=arm)

arm2 = mcomps.optics.Arm(name='arm2')
instrument.append(arm2, position=(0.0, 0.0, 0.0), orientation=(0.0, 'ROT', 0.0), relativeTo=target)

PSD_4pi = mcomps.monitors.PSD_monitor_4PI(name='PSD_4pi', nx=101, ny=51, radius=10, filename="vanadium.psd")
instrument.append(PSD_4pi, position=(0.0, 0.0, 0.0), orientation=(0, 0, 0), relativeTo=arm2)
