import os, numpy as np
import mcvine, mcvine.components as mcomps


def instrument(sample='mcstas', debug=False):
    instrument = mcvine.instrument()
    from mcni.utils import conversion
    a = 4.04932
    ki = 2*np.pi/a * 4
    Ei = conversion.k2e(ki)
    source = mcomps.sources.Source_simple(
        name='source',
        E0=Ei, dE=Ei*1e-10,
        height = 1e-10, width = 1e-10, radius=0,
        dist=10,
        xw = 1e-10, yh = 1e-10,
    )
    instrument.append(source, position=(0.0, 0.0, 0.0), orientation=(0, 0, 0))

    save_src = mcomps.monitors.NeutronToStorage(name='save_src', path='incident.mcv')
    instrument.append(
        save_src, position=(0, 0, 0), orientation=(0,0,0),
        relativeTo=source
    )

    if sample=='mcstas':
        sample = mcomps.samples.Single_crystal(
            reflections = 'Al.lau',
            xwidth = 0.01, yheight = 0.01, zthick = 0.01,
            delta_d_d = 1e-4, mosaic = 5.,
            ax = 4.04932, ay=0., az=0.,
            bx = 0., by=4.04932, bz=0.,
            cx = 0., cy=0., cz=4.04932,
            p_transmit = 0.,
            absorption = 0., incoherent = 0.,
            powder=0,
        )
    elif sample=='mcvine':
        sample = mcomps.samples.SampleAssemblyFromXml('sample', './Al-sc/sampleassembly.xml')
    instrument.append(sample, position=(0., 0., 10.), orientation=(0,0,0))

    save = mcomps.monitors.NeutronToStorage(name='save', path='scattered.mcv')
    instrument.append(
        save, position=(0, 0, 0), orientation=(0,0,0),
        relativeTo=sample
    )
    return instrument

if __name__ == '__main__': ins = instrument()
