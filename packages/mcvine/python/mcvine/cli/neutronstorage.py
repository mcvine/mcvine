# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

from . import mcvine, click

@mcvine.group(help='Commands to manipulate neutron storage')
def neutronstorage():
    return

@neutronstorage.command()
@click.argument("path")
def count(path):
    from mcni.neutron_storage.idf_usenumpy import count
    print count(path)
    return


@neutronstorage.command()
@click.argument("inputpath")
@click.argument("outputpath")
@click.option("--start", default=0, help='start index')
@click.option("--end", default=None, type=int, help='stop index')
def extract(inputpath, outputpath, start, end):
    if start >= end:
        raise ValueError, "Not a valid range: %s, %s" % (
            start, end)

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
            raise RuntimeError, '%s does not exist' % f

    if os.path.exists(out):
        raise RuntimeError, '%s already exists' % out

    from mcni.neutron_storage.merge import merge
    merge(ifiles, out)
    return



# End of file 
