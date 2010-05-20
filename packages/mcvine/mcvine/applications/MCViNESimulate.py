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
            self.help()
            print
            print "** Error: component list is empty"
            print
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
        print 'Example:'
        print 
        print ' mcvine-simulate --components=source,sample,monitor --- --source=MonochromaticSource --source.Ei=...'
        print
        print ' * The first option "--components=..." must be followed with the option splitter "---"'
        print ' * The option "---components" specify the names of neutron components in the instrument'
        print ' * The options after the option splitter "---" provides details of neutron components'
        print 
        print 'How to specify details of neutron components'
        print 'First you need to specify what type of component each component is.'
        print 'And this is done in the form of: '
        print 
        print ' --<componentname>=<componentspecifier>'
        print 
        print 'For example'
        print ' --source=MonochromaticSource'
        print
        print 'The component specifier can be supplied in several different forms:'
        print
        print '''
         * <componentname>
           eg. MonochromaticSource
         * <componentname>.<componentcategory>
           eg. MonochromaticSource.sources
         * <componentname>@<supplier>
           eg. MonochromaticSource@mcni
         * <componentname>.<componentcategory>@<supplier>
           eg. MonochromaticSource.sources@mcni
'''
        print
        print 'See also:'
        print
        print ' mcvine-list-components, mcvine-component-info'
        print 
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
