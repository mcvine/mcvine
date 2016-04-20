#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from .MPILauncherBase import MPILauncherBase as Launcher


class LauncherSlurm(Launcher):


    def __init__(self):
        super(LauncherSlurm, self).__init__("slurm")
        return

    def _defaults(self):
        self.inventory.command = "srun"
        self.inventory.nodesopt = "-n"
        self.inventory.python_mpi = "python-mpi"
        return
    
# End of file 
