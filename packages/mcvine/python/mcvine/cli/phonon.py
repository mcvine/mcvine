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
def band(phonon, start, end, npts):
    "Plot band structure along one direction"
    # phonon is the path to a directory with IDF phonon data
    from mccomponents.sample.phonon import periodicdispersion_fromidf as pd
    import mcni, numpy as np
    disp = pd(phonon)
    import mccomponents.homogeneous_scatterer as mh
    cdisp = mh.scattererEngine(disp)
    Qs = np.array(start) + (np.array(end)-np.array(start)) * np.arange(0, 1, 1./npts)[:, np.newaxis]
    Es = [cdisp.energy(0, mcni.vector3(*Q)) for Q in Qs]
    import pylab
    pylab.plot(Es)
    pylab.show()
    return


# End of file 
