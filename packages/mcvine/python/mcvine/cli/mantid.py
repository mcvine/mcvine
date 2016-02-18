# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

from . import mcvine, click
import h5py, numpy as np


@mcvine.group()
def mantid():
    return

@mantid.command()
@click.argument("mantid")
@click.argument("histogram")
def extract_iqe(mantid, histogram):
    "extract iqe from a mantid-saved h5 file and save to a histogram"
    inpath, outpath = mantid, histogram
    f = h5py.File(inpath)
    w = f['mantid_workspace_1']['workspace']
    e = np.array(w['axis1'])
    de = e[1] - e[0]
    ee = (e+de/2.)[:-1]
    q = np.array(w['axis2'])
    dq = q[1] - q[0]
    qq = (q+dq/2.)[:-1]
    I = np.array(np.array(w['values']))
    # I[I!=I] = 0
    E2 = np.array(np.array(w['errors'])**2)
    import histogram as H
    iqe = H.histogram('iqe', [('Q',qq,  'angstrom**-1'), ('energy', ee, 'meV')], data=I, errors = E2)
    import histogram.hdf as hh
    hh.dump(iqe, outpath)
    return


# End of file 
