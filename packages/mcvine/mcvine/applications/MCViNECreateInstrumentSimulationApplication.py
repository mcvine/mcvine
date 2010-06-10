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


from pyre.applications.Script import Script as base


class Application(base):

    class Inventory(base.Inventory):

        import pyre.inventory

        component_list = pyre.inventory.list('components')
        component_list.meta['tip'] = 'list of component names'

        name = pyre.inventory.str('name')
        name.meta['tip'] = 'name of the simulation application'

        filename = pyre.inventory.str('filename')
        filename.meta['tip'] = 'path of the application that will be created. if not specified, will default the be the same as the <name>'
        
        
    def help(self):
        print
        print 70*'='
        print "%s - Create a mcvine instrument simulation application" % self.name
        print 70*'-'
        print '* Synopsis:'
        print " $ %s --name=<application name> --components=<list of components>" % self.name
        print " $ %s --name=<application name> --components=<list of components> --filename=<application filename>" % self.name
        print 
        print "* Examples:"
        print " $ %s --name='test' --components=source,monitor" % self.name
        print 70*'='
        print
        return


    def main(self):
        name = self.inventory.name
        component_list = self.inventory.component_list

        if not name:
            self.help()
            print '** Error: application name is not specified'
            print
            return
        if not component_list:
            self.help()
            print '** Error: component list is not specified'
            print
            return

        d = {'name': name,
             'components': component_list}
        code = template % d

        cmd = _getCmdStr()
        code += '\n# This application was created by the following command:\n# $ %s\n' % cmd
        code += '\n'
        
        filename = self.inventory.filename
        if not filename:
            filename = name
        open(filename, 'w').write(code)

        import os, stat
        path = os.path.abspath(filename)
        os.chmod(path, stat.S_IRWXU)
        print 'application %r created at %r' % (name, path)
        return



def _getCmdStr():
    import sys, os
    argv = list(sys.argv)
    argv[0] = os.path.basename(argv[0])
    return ' '.join(argv)


template = """#!/usr/bin/env python
import warnings
warnings.simplefilter('ignore')
import mcvine
warnings.simplefilter('default')

def main():
    from mcvine.applications.InstrumentBuilder import build
    components = %(components)r
    App = build(components)
    app = App(%(name)r)
    app.run()
    return

if __name__ == '__main__': main()
"""


# version
__id__ = "$Id$"

# End of file 
