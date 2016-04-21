#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# Launchers
class launchers:
    from .LauncherMPICH2 import LauncherMPICH2 as mpich2
    from .LauncherSlurm import LauncherSlurm as slurm
    from .LauncherSerial import LauncherSerial as serial

ENVVAR_MPI_LAUNCHER = "MCVINE_MPI_LAUNCHER"
import os
mpi_launcher_choice = os.environ.get(ENVVAR_MPI_LAUNCHER, 'mpich2')



## base class of mpi application. derived from pyre mpi application.
## The customization done here are:
##  1. use mpich2 launcher


from .MpiAppBase import Application as base


# check whether mpi is really available by checking the size
# of the mpi world
_usempi = None
def usempi():
    global _usempi
    if _usempi is None:
        from ..utils import mpi
        world = mpi.world
        _usempi = world is not None
        # if mpi.size < 2:
        #    _usempi = False
    return _usempi


class Application(base):

    class Inventory(base.Inventory):

        import pyre.inventory as pinv

        pass # end of Inventory


    def _defaults(self):
        base._defaults(self)
        factory = getattr(launchers, mpi_launcher_choice)
        self.inventory.launcher = factory()
        return


    def onServer(self, *args, **kwds):
        self._debug.log("%s: onServer" % self.name)

        launcher = self.inventory.launcher
        launched = launcher.launch()
        if not launched:
            raise RuntimeError, "application not launched"
        
        return


    def _init(self):
        # if I am not really using mpi, I am a worker
        if usempi():
            if self.inventory.launcher.nodes < 2:
                self.inventory.mode = 'worker'
                global _usempi
                _usempi = False
        else:
            if self.inventory.launcher.nodes > 1:
                msg="Requested for parallel computing but mpi is not available"
                raise RuntimeError(msg)
            self.inventory.mode = 'worker'

        super(Application, self)._init()
        
        return
    
    
    pass # end of Application


# End of file 
