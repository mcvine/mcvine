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
actionname = 'info'

import os
def run(*args, **kwds):
    from mcni.utils import mpi
    print
    print "* mpi binding: %s" % mpi.binding_name
    print
    print "To set mpi binding for mcvine, use env var %r" % mpi.ENVVAR_BINDING_NAME
    print
    return


def parse_cmdline():
    print ("%s %s %s: show information regarding mpi engine used by mcvine\n" % (cliname, cmdname, actionname))
    
    import optparse
    cmd1 =  "%prog " + cmdname + " " + actionname
    usage = "usage: " + cmd1 + " [options]\n"
    usage += "\n * Example:\n"
    usage += "   $ " + cmd1 + ""
    
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    #
    # parser.add_option('-p', '--port', type="int", default=18861, dest='port')
    # parser.add_option('-t', '--type', default='', dest='type')
    
    #
    options, args = parser.parse_args()
    if len(args) > 2:
        parser.error("too many arguments\n\n")

    # filename = options.filename
    # if filename and not os.path.exists(filename):
    #    parser.error("File %s does not exist" % filename)

    kwds = vars(options)
    return args[:], kwds


# version
__id__ = "$Id$"

# End of file 
