#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from .MPILauncherBase import MPILauncherBase as Launcher


class LauncherMPICH2(Launcher):


    def __init__(self):
        super(LauncherMPICH2, self).__init__("mpirun")
        return

    
# End of file 
