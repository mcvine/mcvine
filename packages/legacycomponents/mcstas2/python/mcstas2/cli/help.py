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


import os

def run(*args, **kwds):
    from . import actions
    print()
    print('actions:')
    for action in actions:
        print(('  %s %s %s' % (cliname, cmdname, action)))
        continue
    return
    

def parse_cmdline():
    return [], {}



# version
__id__ = "$Id$"

# End of file 
