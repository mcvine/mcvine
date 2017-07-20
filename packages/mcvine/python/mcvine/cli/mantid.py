# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

from . import mcvine, click

@mcvine.group()
def mantid():
    return

@mantid.command()
@click.argument("mantid_nxs")
@click.argument("histogram")
def extract_iqe(mantid_nxs, histogram):
    "extract iqe from a mantid-saved h5 file and save to a histogram"
    import h5py, numpy as np
    import histogram as H
    inpath, outpath = mantid_nxs, histogram
    f = h5py.File(inpath)
    w = f['mantid_workspace_1']['workspace']
    I = np.array(np.array(w['values']))
    E2 = np.array(np.array(w['errors'])**2)
    # axes
    Naxes = len(I.shape)
    axes = []
    for i in range(Naxes):
        axisds = w['axis%d' % (i+1,)]
        a = np.array(axisds)
        da = a[1] - a[0]
        if a.size == I.shape[Naxes-1-i]+1:
            aa = (a+da/2.)[:-1]
        elif a.size == I.shape[Naxes-1-i]:
            aa = a
        else:
            raise RuntimeError("Dimension mismatch: size(axis %s)=%s, shape(I)=%s" % (i, a.size, I.shape))
        attrs = axisds.attrs
        name=attrs.get('label') or attrs.get('caption')
        if name is None: 
            name = attrs.get('units') # this is really strange
        # unit=attrs.get('units')
        axis = H.axis(name, centers=aa) # unit=unit,
        axes.append(axis)
        continue
    # I[I!=I] = 0
    hname =  ''.join(f['mantid_workspace_1']['workspace_name'])
    iqe = H.histogram(hname, axes, data=I.T, errors = E2.T)
    import histogram.hdf as hh
    hh.dump(iqe, outpath)
    return


# End of file 
