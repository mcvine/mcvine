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


name = 'mcstas'


def run(mod, *args, **opts):
    return mod.run(*args, **opts)


def importActionHandler(action):
    code = 'from . import %s' % action
    exec(code)
    mod = locals()[action]
    if mod is None:
        raise ImportError(action)
    return mod


def parse_cmdline():
    import sys
    if len(sys.argv) <= 2:
        action = 'help'
    else:
        action = sys.argv[2]

    if action in ['-h', '--help']:
        action = 'help'

    if action not in actions:
        print ()
        print ("Invalid action: %s" % action)
        action = 'help'
    
    mod = importActionHandler(action)
    args, kwds = mod.parse_cmdline()
    return [mod] + args, kwds


actions = [
    'compilecomponent',
    'convertinstrument',
    'help',
    ]


# version
__id__ = "$Id$"

# End of file 
