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

import os

from . import name

def run(*args, **kwds):
    from . import public_commands
    print()
    print('Basic commands:')
    for cmd in public_commands:
        print('  %s %s' % (name, cmd))
        continue
    return
    

def parse_cmdline():
    return [], {}


# version
__id__ = "$Id$"

# End of file 
