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


class LauncherMPICH2(Launcher):


    class Inventory(Launcher.Inventory):

        import pyre.inventory

        dry = pyre.inventory.bool("dry", default=False)
        debug = pyre.inventory.bool("debug", default=False)
        command = pyre.inventory.str("command", default="mpirun")
        extra = pyre.inventory.str("extra", default="")
        python_mpi = pyre.inventory.str("python-mpi", default="`which python`")


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
        if not python_mpi:
            python_mpi = self._get_python_mpi()

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
