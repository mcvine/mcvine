#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                             Michael A.G. Aivazis
#                      California Institute of Technology
#                      (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .LauncherBase import Launcher


class LauncherSerial(Launcher):


    class Inventory(Launcher.Inventory):

        import pyre.inventory
        dry = pyre.inventory.bool("dry", default=False)

    def launch(self):
        args = self._buildArgumentList()
        if not args:
            return False
        
        command = " ".join(args)
        self._info.log("executing: {%s}" % command)

        dry = self.inventory.dry
        if not dry:
            import os
            if os.system(command):
               raise RuntimeError("%s failed" % command) 
            return True

        return False

            
    def __init__(self, name='serial'):
        Launcher.__init__(self, name=name)
        return

    
    def _buildArgumentList(self):
        import sys
        # build the command
        args = ['python']
        sysargs = sys.argv
        args.append( sysargs[0] )
        args.append("--mode=worker")
        args += sysargs[1:]
        return args


# version
__id__ = "$Id$"

# End of file 
