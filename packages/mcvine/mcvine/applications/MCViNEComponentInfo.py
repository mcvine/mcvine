#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
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


    def help(self):
        print
        print 70*'='
        print '%s - Display information about a mcvine component type' % self.name
        print 70*'-'
        print '* Synopsis:'
        print ' $ %s --supplier=<supplier> --category=<category> --type=<type>' % self.name
        print 
        print '* Examples:'
        print ' $ %s --type=Source_simple' % self.name
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
        print componentinfo(category=category, type=type, supplier=supplier)
        return


    def _configure(self):
        super(Application, self)._configure()
        self.supplier = self.inventory.supplier
        self.category = self.inventory.category
        self.type = self.inventory.type
        return


# version
__id__ = "$Id$"

# End of file 
