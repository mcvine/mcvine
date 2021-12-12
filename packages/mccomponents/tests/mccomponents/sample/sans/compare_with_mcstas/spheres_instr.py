#!/usr/bin/env python
import os
thisdir = os.path.dirname(__file__)
import mcvine, mcvine.components as mc
def instrument(E0=10, sample_vendor='mcstas'):
    instrument = mcvine.instrument()
    source = mc.sources.Source_simple(
        'source',
        E0=E0, dE=E0*0.01, radius=0.01, dist=20., xw=0.01, yh=0.01)
    instrument.append(source, position=(0,0,0))
    if sample_vendor == 'mcstas':
        sample = mc.samples.Sans_spheres(
            name='sample', R = 100, Phi = 1e-3, Delta_rho = 0.6, sigma_a = 50,
            xwidth=0.01, yheight=0.01, zthick=0.005,
            Rdet = 0.5, dist = 10.,
        )
        sample = mc.samples.Sans_spheres(
            name='sample', R = 500, Phi = 0.1, Delta_rho = 0.6,
            # sigma_a = 0.05,
            sigma_a = 0.,
            xwidth=0.01, yheight=0.01, zthick=0.001,
            Rdet = 0.5, dist = 10.,
        )
    elif sample_vendor == 'mcvine':
        samplexml = os.path.join(
            thisdir, '../xml/sampleassemblies/sans_spheres/sampleassembly.xml')
        sample = mc.samples.SampleAssemblyFromXml('sample', samplexml)
    else:
        raise NotImplementedError(sample_vendor)
    instrument.append(sample, position=(0,0,20))
    # after_sample = mc.monitors.NeutronToStorage("after_sample", path="after_sample.mcv")
    # instrument.append(after_sample, position=(0,0,20))
    # monitor = mc.monitors.PSD_monitor(
    #     'monitor', filename='Ixy.dat',
    #     xwidth=1, yheight=1, nx=250, ny=250,
    # )
    from mcni.utils import conversion
    ki = conversion.e2k(E0)
    from mcni.components.NDMonitor import Axis
    expr = "%s*sqrt(x*x+y*y)/%s" % (ki, 10.)
    axes = [Axis(name='q', expression=expr, range=(0, 0.1), bins=250, unit='1./angstrom')]
    monitor = mc.monitors.NDMonitor("I_q", axes = axes, size = (1., 1.))
    instrument.append(monitor, position=(0,0,30))
    return instrument


def main():
    from mcvine import run_script
    ncount = 1e9
    outdir = 'out.mcstas_spheres-%g' % (ncount,)
    run_script.run_mpi(__file__, outdir, ncount=ncount, nodes=24, overwrite_datafiles=True)
    return

if __name__ == '__main__': main()
