# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

encoding = 'UTF-8'

from . import mcvine, click

@mcvine.group(help='Commands related to mcvine simulation component')
def component():
    return

def _info_help(name):
    l = []
    l.append(70*'=')
    l.append('%s - Display information about a mcvine component type' % name)
    l.append(70*'-')
    l.append('* Synopsis:')
    l.append(' $ %s <type>' % name)
    l.append(' $ %s <type> --args=<args>' % name)
    l.append(' $ %s <type> --supplier=<supplier> --category=<category> --args=<args>' % name)
    l.append('')
    l.append('* Examples:')
    l.append(' $ %s Source_simple' % name)
    l.append(' $ %s NDMonitor --args=x,y' % name)
    l.append(' $ %s Source_simple --supplier=mcstas2 --category=sources' % name)
    l.append(70 * '-')
    l.append('* See also:')
    l.append('   mcvine component list')
    l.append(70*'=')
    l.append('')
    return '\n\n'.join(l)
@component.command(help=_info_help('mcvine component info'))
@click.argument("type", type=str)
@click.option(
    "--category", type=str, default=None,
    help=('category of the component.' +
          'Components are organized into several categories ' +
          '(following mcstas convention) such as sources and '+
          'monitors. If not specified, auto-detection will happen.')
)
@click.option(
    "--args", default='',
    help=('(component dependent) arguments for the component.' +
          'Most components don\'t need additional arguments, a few '+
          'components do. See below for some examples.')
)
@click.option(
    "--supplier", type=str, default=None,
    help=('supplier of the component. In mcvine, components could come from legacy Monte Carlo neutron packages. '\
          +'If not specified, auto-detection will happen.')
)
def info(type, category, args, supplier):
    type = type.encode(encoding)
    if args:
        args = args.encode(encoding)
        args = args.split(',')
    if category:
        category = category.encode(encoding)
    if supplier:
        supplier = supplier.encode(encoding)
    from mcvine.pyre_support import componentinfo
    print componentinfo(*args, type=type, category=category, supplier=supplier)
    print
    print "To use this component, use the specifier"
    print
    specifier = _getSpecifier(*args, type=type, category=category, supplier=supplier)
    print "   %s" % specifier
    print 
    print "E.g."
    print
    print '   --component1="%s"' % specifier
    print
    return
def _getSpecifier(*args, **kwds):
    # this is a simplified implementation
    type = kwds['type']
    argsstr = ''
    if args:
        argsstr = '(%s)' % (','.join(args),)
    return '%s%s' % (type, argsstr)



@component.command()
@click.argument("path")
def totalintensity(path):
    from mcni.neutron_storage.idf_usenumpy import read
    neutrons = read(path)
    probs = neutrons[:, 9]
    totalIntensity = probs.sum()
    print totalIntensity
    return


@component.command()
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


@component.command()
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

    from mcni.neutron_storage import merge
    merge(ifiles, out)
    return


@component.command("print")
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
        raise ValueError, "Not a valid range: start=%s, end=%s, n=%s" % (
            start, end, n)
    #
    from mcni.neutron_storage.Storage import Storage
    storage = Storage(path)
    storage.seek(start, 'start')
    neutrons = storage.read(n)
    for e in neutrons:
        print e
    return


# End of file 
