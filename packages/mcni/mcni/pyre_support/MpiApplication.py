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


## base class of mpi application. derived from pyre mpi application.
## The customization done here are:
##  1. use mpich2 launcher


try:
    from mpi.Application import Application as base
    usempi = True
except ImportError:
    import warnings
    msg = "mpi python module not available. parallel simulation is not supported"
    warnings.warn( msg )
    from pyre.applications.Script import Script as base
    usempi = False


class Application(base):

    class Inventory(base.Inventory):

        import pyre.inventory as pinv

        pass # end of Inventory


    if usempi:
        def _defaults(self):
            base._defaults(self)
            from LauncherMPICH2 import LauncherMPICH2
            self.inventory.launcher = LauncherMPICH2()
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
        global usempi
        if usempi and self.inventory.launcher.nodes == 1:
            self.inventory.mode = 'worker'
            usempi = False
        if not usempi:
            self.inventory.mode = 'worker'
        if usempi and not self.inventory.launcher.nodes:
            self.inventory.mode = 'worker'

        super(Application, self)._init()
        
        return
    
    
    pass # end of Application



# version
__id__ = "$Id$"

# End of file 
