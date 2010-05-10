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

from SuperAppBase import SuperAppBase


class Application(SuperAppBase):

    class Inventory(SuperAppBase.Inventory):

        import pyre.inventory

        component_list = pyre.inventory.list('components')
        component_list.meta[SuperAppBase.inventory_item_signature] = True


    def runApp(self, components=None, **kwds):
        from InstrumentBuilder import build
        components = self.component_list
        if not components:
            print "* Error: component list is empty"
            self.help()
            return
        Instrument = build(components)
        instrument = Instrument('mcvine-instrument')
        return instrument.run()


    def help(self):
        print
        print 'simulate a neutron instrument'
        print
        print ' mcvine-simulate --components=<list-of-components> --- <configrations of components>'
        print 
        print 'Examples:'
        print 
        print ' mcvine-simulate --components=source,sample,monitor --- --source=monochromatic --source.Ei=...'
        print
        print 'See also:'
        print
        print ' mcvine-list-components, mcvine-component-info'
        return

    
    def _configure(self):
        super(Application, self)._configure()
        self.component_list = self.inventory.component_list
        return


    def _defaults(self):
        super(Application, self)._defaults()
        self.inventory.typos = 'relaxed'
        return



# version
__id__ = "$Id$"

# End of file 
