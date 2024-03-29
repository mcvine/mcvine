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


import os, sys
from .LauncherBase import Launcher


class MPILauncherBase(Launcher):


    class Inventory(Launcher.Inventory):

        import pyre.inventory

        dry = pyre.inventory.bool("dry", default=False)
        debug = pyre.inventory.bool("debug", default=False)
        command = pyre.inventory.str("command", default="mpirun")
        nodesopt = pyre.inventory.str("nodes-opt", default="-np")
        extra = pyre.inventory.str("extra", default="")
        python_mpi = pyre.inventory.str("python-mpi", default=os.path.abspath(sys.executable))


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


    def _buildArgumentList(self):
        import sys

        nodes = self.nodes
        self._debug.log(
            'nodes = %d, self.inventory.nodes = %d' % (
            nodes, self.inventory.nodes )
            )
        python_mpi = self.inventory.python_mpi
        if not python_mpi:
            python_mpi = self._get_python_mpi()

        if nodes < 2:
            self.inventory.nodes = nodes = 1
        
        # build the command
        args = []
        args.append(self.inventory.command)
        args.append(self.inventory.extra)

        args.append("%s %d" % (self.inventory.nodesopt, nodes))

        # add the parallel version of the interpreter on the command line
        args.append(python_mpi)

        sysargs = sys.argv
        args.append( sysargs[0] )
        args.append("--mode=worker")
        for arg in sysargs[1:]:
            index = arg.find('=')
            if index == -1:
                args.append(arg)
                continue
            k = arg[:index]
            v = arg[index+1:]
            args.append('%s="%s"' % (k,v))
            continue

        return args


# version
__id__ = "$Id$"

# End of file 
