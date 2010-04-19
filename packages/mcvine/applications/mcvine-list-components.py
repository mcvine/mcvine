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

class App(Script):

    class Inventory(Script.Inventory):

        import pyre.inventory

        supplier = pyre.inventory.str('supplier')
        supplier.meta['tip'] = 'supplier of mcvine components. eg. mcstas2'
        
        category = pyre.inventory.str('category')
        category.meta['tip'] = 'category of mcvine components. eg. sources'

    
    def main(self, *args, **kwds):
        from mcvine.component_suppliers import component_suppliers
        from mcvine import listallcomponentcategories, listcomponentsincategory
        
        suppliername = self.supplier
        category = self.category
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


    def __init__(self, name='mcvine-list-components'):
        super(App, self).__init__(name)
        return


    def _configure(self):
        super(App, self)._configure()
        self.supplier = self.inventory.supplier
        self.category = self.inventory.category
        return


def main():
    app = App()
    app.run()
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
