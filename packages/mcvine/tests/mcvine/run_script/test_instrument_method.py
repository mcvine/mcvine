def instrument(E0=60):
    import mcvine, mcvine.components
    instrument = mcvine.instrument()
    # add source
    source = mcvine.components.sources.Source_simple('source', E0=E0)
    instrument.append(source, position=(0,0,0))
    # add monitor
    monitor = mcvine.components.monitors.E_monitor('monitor', filename='IE.dat', Emin=10, Emax=120)
    instrument.append(monitor, position=(0,0,1))
    return instrument
