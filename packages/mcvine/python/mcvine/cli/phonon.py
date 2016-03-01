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
    disp = pd(phonon)
    import mccomponents.homogeneous_scatterer as mh
    cdisp = mh.scattererEngine(disp)
    return


# End of file 
