#!/usr/bin/env python
#

# copied from pyre: mpi.Application


from pyre.applications.Script import Script


class Application(Script):


    class Inventory(Script.Inventory):

        import pyre.inventory

        from .LauncherSerial import LauncherSerial

        mode = pyre.inventory.str(
            name="mode", default="server", validator=pyre.inventory.choice(["server", "worker"]))
        launcher = pyre.inventory.facility("launcher", factory=LauncherSerial)


    def execute(self, *args, **kwds):

        if self.inventory.mode == "worker":
            self.onComputeNodes(*args, **kwds)
            return
        
        self.onServer(*args, **kwds)

        return


    def onComputeNodes(self, *args, **kwds):
        from ..utils import mpi
        import logging
        logger = logging.getLogger("MCVine")
        logger.debug("size=%s, rank=%s" % (mpi.size, mpi.rank))
        self.main(*args, **kwds)
        return


    def onServer(self, *args, **kwds):
        self._debug.log("%s: onServer" % self.name)

        launcher = self.inventory.launcher
        launched = launcher.launch()
        if not launched:
            self.onComputeNodes(*args, **kwds)
        
        return


    def __init__(self, name):
        Script.__init__(self, name)
        self.launcher = None
        return


    def _configure(self):
        Script._configure(self)
        self.launcher = self.inventory.launcher
        return


# version
__id__ = "$Id$"

# End of file 
