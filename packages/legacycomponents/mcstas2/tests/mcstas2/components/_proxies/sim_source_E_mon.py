# sim_source_E_mon.py

import numpy as np
import mcvine, mcvine.components as mcomps

def instrument():
    instrument = mcvine.instrument()
    
    src = mcomps.sources.Source_simple(name='player', dist=1., E0=500, dE=200, gauss=0)
    instrument.append(src, position=(0.,0,0), orientation=(0,0,0))
    
    E_det = mcomps.monitors.E_monitor(
        name='E_det', nchan=2,
        xmin=-.05, xmax=.05, ymin=-.025, ymax=.05,
        Emin=0, Emax=10000.,
        filename='E.dat', )
    instrument.append(E_det, position=(0.0, 0.0, 1.001), orientation=(0, 0, 0))
    
    return instrument

