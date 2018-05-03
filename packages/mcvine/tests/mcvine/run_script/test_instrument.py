import mcvine
instrument = mcvine.instrument()
# add source
source = mcvine.components.sources.Source_simple('source')
instrument.append(source, position=(0,0,0))
# add monitor
monitor = mcvine.components.monitors.E_monitor('monitor', filename='IE.dat')
instrument.append(monitor, position=(0,0,1))
