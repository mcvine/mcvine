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


from mpi.Launcher import Launcher


class LauncherMPICH2(Launcher):


    class Inventory(Launcher.Inventory):

        import pyre.inventory

        dry = pyre.inventory.bool("dry", default=False)
        debug = pyre.inventory.bool("debug", default=False)
        command = pyre.inventory.str("command", default="mpirun")
        extra = pyre.inventory.str("extra", default="")
        python_mpi = pyre.inventory.str("python-mpi", default="`which mpipython.exe`")


    def launch(self):
        args = self._buildArgumentList()
        if not args:
            return False
        
        command = " ".join(args)
        self._info.log("executing: {%s}" % command)

        dry = self.inventory.dry
        if not dry:
            import os
            os.system(command)
            return True

        return False

            
    def __init__(self):
        Launcher.__init__(self, "mpirun")
        return


    def _buildArgumentList(self):
        import sys

        nodes = self.nodes
        self._debug.log(
            'nodes = %d, self.inventory.nodes = %d' % (
            nodes, self.inventory.nodes )
            )
        python_mpi = self.inventory.python_mpi

        if nodes < 2:
            self.inventory.nodes = 1
            return []
        
        # build the command
        args = []
        args.append(self.inventory.command)
        args.append(self.inventory.extra)

        args.append("-np %d" % nodes)

        # add the parallel version of the interpreter on the command line
        args.append(python_mpi)

        sysargs = sys.argv
        args.append( sysargs[0] )
        args.append("--mode=worker")
        args += sysargs[1:]

        return args


# version
__id__ = "$Id: LauncherMPICH2.py,v 1.1.1.1 2005/03/08 16:13:30 aivazis Exp $"

# End of file 
