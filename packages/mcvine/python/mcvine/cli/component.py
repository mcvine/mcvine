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
@click.option(
    "--category", type=str, default=None,
    help=('category of the component.' +
          'Components are organized into several categories ' +
          '(following mcstas convention) such as sources and '+
          'monitors. If not specified, auto-detection will happen.')
)
@click.option(
    "--supplier", type=str, default=None,
    help=('supplier of the component. In mcvine, components could come from legacy Monte Carlo neutron packages. '\
          +'If not specified, auto-detection will happen.')
)
def list(category, supplier):
    if category:
        category = category.encode(encoding)
    if supplier:
        supplier = supplier.encode(encoding)
    suppliername = supplier
    
    from mcvine.component_suppliers import component_suppliers
    from mcvine import listallcomponentcategories, listcomponentsincategory

    if suppliername:
        supplier = component_suppliers.get(suppliername)
        if not supplier:
            print 'supplier %r not found. use command mcinve-list-componnet-suppliers to see the supplier list' % suppliername
            import sys
            sys.exit(1)

        if category:
            comps = supplier.listcomponentsincategory(category)
            print ' - components in %r category provided by %r' % (category, suppliername)
            for comp in comps:
                print '  * %s' % comp

        else:
            for category in supplier.listallcomponentcategories():
                print ' - components in %r category provided by %r' % (category, suppliername)
                comps = supplier.listcomponentsincategory(category)
                for comp in comps:
                    print '  * %s' % comp
                print
    else:
        if category:
            print ' - components in %r category' % (category,)
            comps = listcomponentsincategory(category)
            for comp, suppliername in comps:
                print '  * %s (from %r)' % (comp, suppliername)
        else:
            for category in listallcomponentcategories():
                print ' - components in %r category' % (category,)
                comps = listcomponentsincategory(category)
                for comp, suppliername in comps:
                    print '  * %s (provided by %r)' % (comp, suppliername)
                print
    return



# End of file 
