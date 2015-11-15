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
actionname = 'simiqe'

import os
def run(xml, **kwds):
    print (xml, kwds)
    return


def parse_cmdline():
    print ("%s %s %s: sim I(Q,E) spectrum of a kernel\n" % (cliname, cmdname, actionname))
    
    import optparse
    usage = "usage: %prog " + cmdname + " " + actionname + " scattererxml [options]"
    
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    #
    # parser.add_option('-p', '--port', type="int", default=18861, dest='port')
    
    #
    options, args = parser.parse_args()
    if len(args) > 3:
        parser.error("too many arguments\n\n")
    if len(args) == 2:
        parser.error("please specify path to sample scatterer xml file")
        
    args, kwds = args[2:], vars(options)
    return args, kwds


# version
__id__ = "$Id$"

# End of file 
