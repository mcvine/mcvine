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
        base = build(components)
        class Instrument(base):
            def _defaults(self):
                super(Instrument, self)._defaults()
                # can only run serially
                self.inventory.mode = 'worker'
                from mcni.pyre_support.LauncherSerial import LauncherSerial
                self.inventory.launcher = LauncherSerial()
                return
        instrument = Instrument('mcvine-instrument')
        return instrument.run()


    def help(self):
        print
        print 70*'='
        print 'mcvine-simulate - run a mcvine simulation'
        print 70*'-'
        print '* Synopsis'
        print ' $ mcvine-simulate --components=<list-of-components> --- \\'
        print '                 <configrations of components>'
        print 70*'-'
        print '* Example 1:'
        print ' $ mcvine-simulate --components=source,monitor --- \\'
        print '                 --geometer.source=[0,0,0],[0,0,0] \\'
        print '                 --source=MonochromaticSource --source.Ei=... \\'
        print '                 --monitor=E_monitor --monitor.Emin=... \\'
        print
        print ' * The first option "--components=..." must be followed with'
        print '   the option splitter "---"'
        print ' * The option "--components" specify the names of neutron '
        print '   components in the instrument'
        print ' * The options after the option splitter "---" provides details'
        print '   of neutron components'
        print '   * Geometer'
        print '       --geometer.<compoenntname>=<position>,<orientation>'
        print '     eg.'
        print '       --geometer.source=[0,0,0],[0,0,0]'
        print '   * Component type'
        print '       --<componentname>=<componentspecifier>'
        print '     eg.'
        print '       --source=MonochromaticSource'
        print '     * See also:'
        print '       mcvine-list-components, mcvine-component-info'
        print '   * Component details'
        print '       --<componentname>.<property>=<value>'
        print '     eg.'
        print '       --source.Ei=60'
        print 70*'='
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
