# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

from . import mcvine, click

@mcvine.group()
def phonon():
    return

@phonon.command()
@click.argument("phonon")
@click.option("--start", default=(0.,0.,0.))
@click.option("--end", default=(0.,0.,1.))
@click.option("--npts", default=100)
@click.option("--cartesian", default=False, is_flag=True)
@click.option("--output", default="")
def band(phonon, start, end, npts, cartesian, output):
    "Plot band structure along one direction"
    # phonon is the path to a directory with IDF phonon data
    from mccomponents.sample.phonon import periodicdispersion_fromidf as pd
    import mcni, numpy as np
    disp = pd(phonon)
    import mccomponents.homogeneous_scatterer as mh
    cdisp = mh.scattererEngine(disp)
    Qs = np.array(start) + (np.array(end)-np.array(start)) * np.arange(0, 1, 1./npts)[:, np.newaxis]
    if not cartesian:
        # read reciprocal basis vectors from Qgridinfo
        import os
        lines = open(os.path.join(phonon, 'Qgridinfo')).readlines(3)
        d = {}
        for line in lines:
            exec(line, d)
            continue
        reci_basis = [d['b1'], d['b2'], d['b3']]
        Qs = np.dot(Qs, reci_basis)
    Es = [cdisp.energy(0, mcni.vector3(*Q)) for Q in Qs]
    import pylab
    pylab.plot(Es)
    if output:
        pylab.savefig(output)
    else:
        pylab.show()
    return


# End of file 
