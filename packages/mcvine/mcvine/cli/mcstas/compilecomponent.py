# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .. import name as cliname
from . import name as cmdname
actionname = 'compilecomponent'

import os
def run(debug=None, type=None, category=None, filename=None):
    if debug:
        import mcstas2
        mcstas2.DEBUG = True

    if filename:
        compileFile(filename, category)
        return
    
    from mcvine import findcomponentfactory
    cf = findcomponentfactory(
        type=type, category=category or None, supplier='mcstas2',
        )
    # instantiate a component will trigger automatic build procedure
    cf()
    return


def compileFile(filename, category):

    from mcstas2 import wrapcomponent
    wrapcomponent(filename, category)
    return


def parse_cmdline():
    print ("%s %s %s: compile a mcstas component\n" % (cliname, cmdname, actionname))
    
    import optparse
    cmd1 =  "%prog " + cmdname + " " + actionname
    usage = "usage: " + cmd1 + " [options]\n"
    usage += "\n * Example:\n"
    usage += "   $ " + cmd1 + " --filename=E_monitor.comp --category=monitors"
    
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    #
    # parser.add_option('-p', '--port', type="int", default=18861, dest='port')
    parser.add_option('-t', '--type', default='', dest='type')
    parser.add_option('-c', '--category', default='', dest='category')
    parser.add_option('-f', '--filename', default='', dest='filename')
    parser.add_option('-d', '--debug', action='store_true', dest='debug')
    
    #
    options, args = parser.parse_args()
    if len(args) > 2:
        parser.error("too many arguments\n\n")

    filename = options.filename
    if filename and not os.path.exists(filename):
        parser.error("File %s does not exist" % filename)

    category = options.category
    if filename and not category:
        parser.error("component category was not specified.")

    type = options.type
    if not filename and not type:
        parser.error("either specify component file path to compile, or a component type name")
        
    kwds = vars(options)
    return args[2:], kwds


# version
__id__ = "$Id$"

# End of file 
