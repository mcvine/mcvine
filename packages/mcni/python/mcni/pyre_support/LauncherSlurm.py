#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from .MPILauncherBase import MPILauncherBase as Launcher


class LauncherSlurm(Launcher):


    def __init__(self):
        super(LauncherSlurm, self).__init__("slurm")
        return

    
# End of file 
