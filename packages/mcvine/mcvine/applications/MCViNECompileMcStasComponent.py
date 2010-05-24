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

        name = pyre.inventory.str('name')
        category = pyre.inventory.str('category')
        filename = pyre.inventory.str('filename')


    def help(self):
        print
        print 'Compile a mcstas component to be usable in mcvine'
        print
        print '%s --filename=<path> --category=<category>' % self.name
        print 
        print 'Examples:'
        print 
        print ' $ %s --filename=E_monitor.comp --category=monitors' % self.name
        print 
        return

    
    def main(self, *args, **kwds):
        filename = self.filename
        import os
        if filename and not os.path.exists(filename):
            self.help()
            print 
            print "** Error: file %s does not exist" % filename
            return

        if filename:
            self.compileFile(filename)
            return

        from mcvine import findcomponentfactory
        cf = findcomponentfactory(
            type=self.type, category=self.category or None, supplier='mcstas2',
            )
        # instantiate a component will trigger automatic build procedure
        cf()
        return

    
    def compileFile(self, filename):
        category = self.category
        if not category:
            self.help()
            print
            print "** Error: component category was not specified."
            return

        from mcstas2 import wrapcomponent
        wrapcomponent(filename, category)
        return


    def _configure(self):
        super(Application, self)._configure()
        self.type = self.inventory.name
        self.category = self.inventory.category
        self.filename = self.inventory.filename
        return


# version
__id__ = "$Id$"

# End of file 
