# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, numpy as np
from . import mcvine, click
from functools import reduce

@mcvine.group(help='Commands to manipulate neutron storage')
def neutronstorage():
    return

@neutronstorage.command()
@click.argument("path")
def count(path):
    from mcni.neutron_storage.idf_usenumpy import count
    print(count(path))
    return

@neutronstorage.command()
@click.argument("path")
def totalintensity(path):
    from mcni.neutron_storage.idf_usenumpy import read
    neutrons = read(path)
    probs = neutrons[:, 9]
    totalIntensity = probs.sum()
    print(totalIntensity)
    return

@neutronstorage.command()
@click.argument("path")
def averageintensity(path):
    from mcni.neutron_storage.idf_usenumpy import read
    neutrons = read(path)
    probs = neutrons[:, 9]
    totalIntensity = probs.sum()
    print(totalIntensity/probs.size)
    return

@neutronstorage.command()
@click.argument("inputpath")
@click.argument("outputpath")
@click.option("--start", default=0, help='start index')
@click.option("--end", default=None, type=int, help='stop index')
def extract(inputpath, outputpath, start, end):
    if start >= end:
        raise ValueError("Not a valid range: %s, %s" % (
            start, end))
    n = end - start
    from mcni.neutron_storage.idf_usenumpy import read, write
    # read neutrons
    neutrons = read(inputpath, start=start, n = n)
    # write them
    write(neutrons, filename=outputpath)
    return

@neutronstorage.command()
@click.option("--files", type=str, help='comma-separated list of files')
@click.option("--out", help='output path')
def merge(files, out):
    import os, glob, operator
    ifiles = [glob.glob(f) for f in files.split(',')]
    ifiles = reduce(operator.add, ifiles)

    for f in ifiles:
        if not os.path.exists(f):
            raise RuntimeError('%s does not exist' % f)

    if os.path.exists(out):
        raise RuntimeError('%s already exists' % out)

    from mcni.neutron_storage import merge
    merge(ifiles, out)
    return

@neutronstorage.command("print")
@click.argument("path")
@click.option("--start", default=0, help='start index')
@click.option("--end", default=None, type=int, help='stop index')
@click.option("--n", default=None, type=int, help='number of neutrons')
def _print(path, start, end, n):
    if end is not None and n is not None:
        raise RuntimeError(
            "Both stop index (%s) and number of neutrons (%s) are specified. Should only specify one of them" % (
                end, n))
    if n is None:
        n = end - start
    if n<=0:
        raise ValueError("Not a valid range: start=%s, end=%s, n=%s" % (
            start, end, n))
    #
    from mcni.neutron_storage.Storage import Storage
    storage = Storage(path)
    storage.seek(start, 'start')
    neutrons = storage.read(n)
    for e in neutrons:
        print(e)
    return

@neutronstorage.command()
@click.argument("path")
@click.option("--out", help='output path')
@click.option("--scale-by-number-of-packets/--no-scale-by-number-of-packets", default=True)
def from_mcpl(path, out, scale_by_number_of_packets):
    try:
        import mcpl
    except ImportError:
        raise RuntimeError("Failed to import mcpl. Please install mcpl python package.")
    from mcni.utils import conversion
    from mcni.neutron_storage.idf_usenumpy import write
    # main loop
    myfile = mcpl.MCPLFile(path)
    base, ext = os.path.splitext(out)
    arrays = []
    for i,pb in enumerate(myfile.particle_blocks):
        x,y,z = pb.x/100., pb.y/100., pb.z/100.
        N1 = x.size
        t = pb.time/1e3
        p = pb.weight
        E = pb.ekin*1e9
        v = conversion.e2v(E)
        vv = v[:, np.newaxis] * pb.direction
        vx,vy,vz = vv.T
        s1 = s2 = np.zeros(N1)
        cond = p>0
        arr = np.array([
            x[cond],y[cond],z[cond],vx[cond],vy[cond],vz[cond],
            s1[cond],s2[cond],t[cond],p[cond]]).T.copy()
        arrays.append(arr)
        # fn = '{}-{}{}'.format(base, i, ext)
        continue
    arr = np.concatenate(arrays); del arrays
    print(arr.shape)
    assert len(arr.shape)==2 and arr.shape[-1]==10
    if scale_by_number_of_packets:
        N = arr.shape[0]
        arr[:, -1] *= N
    write(arr, out)
    return

@neutronstorage.command()
@click.argument("path")
@click.option("--out", help='output path')
@click.option("--renormalize/--no-renormalize", help='rescale the probability to ensure each neutron represents one unit time (for example one pulse from moderator)')
def clean(path, out, renormalize):
    raise NotImplemented
    return

# End of file
