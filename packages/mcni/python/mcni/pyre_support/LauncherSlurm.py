#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, sys

from .MPILauncherBase import MPILauncherBase as Launcher

class LauncherSlurm(Launcher):


    def __init__(self, name='slurm'):
        super(LauncherSlurm, self).__init__(name)
        return

    def _defaults(self):
        self.inventory.command = "srun"
        self.inventory.nodesopt = "-n"
        # self.inventory.python_mpi = "python-mpi"
        self.inventory.python_mpi = os.path.abspath(sys.executable)
        return

# End of file
