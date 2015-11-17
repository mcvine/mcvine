#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from pyre.applications.Script import Script

class Application(Script):

    class Inventory(Script.Inventory):

        import pyre.inventory

        supplier = pyre.inventory.str('supplier')
        supplier.meta['tip'] = 'supplier of mcvine component. eg. mcstas2'
        
        category = pyre.inventory.str('category')
        category.meta['tip'] = 'category of mcvine component. eg. sources'

        type = pyre.inventory.str('type')
        type.meta['tip'] = 'type of mcvine component. eg. Source_simple'

        args = pyre.inventory.list('args')
        args.meta['tip'] = 'args needed for constructing a component in addition to its name'


    def help(self):
        print
        print 70*'='
        print '%s - Display information about a mcvine component type' % self.name
        print 70*'-'
        print '* Synopsis:'
        print ' $ %s --type=<type>' % self.name
        print ' $ %s --type=<type> --args=<args>' % self.name
        print ' $ %s --supplier=<supplier> --category=<category> --type=<type> --args=<args>' % self.name
        print 
        print '* Parameters:'
        print '  -type: '
        print '       (required) type name of the comonent. To see all '
        print '       available components, use command '
        print '       mcvine-list-components'
        print '  -supplier:'
        print '       (optional) supplier of the component. '
        print '       In mcvine, components could come from legacy Monte '
        print '       Carlo neutron packages. If not specified, '
        print '       auto-detection will happen.'
        print '  -category:'
        print '       (optional) category of the component.'
        print '       Components are organized into several categories '
        print '       (following mcstas convention) such as sources and '
        print '       monitors. If not specified, auto-detection will happen.'
        print '  -args:'
        print '       (optional, component dependent) arguments for the component.'
        print '       Most components don\'t need additional arguments, a few '
        print '       components do. See below for some examples.'
        print
        print '* Examples:'
        print ' $ %s --type=Source_simple' % self.name
        print ' $ %s --type=NDMonitor --args=x,y' % self.name
        print ' $ %s --supplier=mcstas2 --category=sources --type=Source_simple' % self.name
        print 70 * '-'
        print '* See also:'
        print '   mcvine-list-components'
        print 70*'='
        print
        return

    
    def main(self, *args, **kwds):
        supplier = self.supplier or None
        category = self.category or None
        type = self.type
        
        #if not supplier or not category or not type:
        #    self.help()
        #    return
        
        from mcvine.pyre_support import componentinfo
        args = self.inventory.args
        print componentinfo(*args, type=type, category=category, supplier=supplier)
        print
        print "To use this component, use the specifier"
        print
        specifier = self._getSpecifier(*args, type=type, category=category, supplier=supplier)
        print "   %s" % specifier
        print 
        print "E.g."
        print
        print '   --component1="%s"' % specifier
        print
        return


    def _getSpecifier(self, *args, **kwds):
        # this is a simplified implementation
        type = kwds['type']
        argsstr = ''
        if args:
            argsstr = '(%s)' % (','.join(args),)
        return '%s%s' % (type, argsstr)
    

    def _configure(self):
        super(Application, self)._configure()
        self.supplier = self.inventory.supplier
        self.category = self.inventory.category
        self.type = self.inventory.type
        return


# version
__id__ = "$Id$"

# End of file 
