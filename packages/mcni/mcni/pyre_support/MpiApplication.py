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
except ImportError:
    import warnings
    msg = "mpi python module not available. parallel simulation is not supported"
    warnings.warn( msg )
    from pyre.applications.Script import Script as base



class Application(base):

    class Inventory(base.Inventory):

        import pyre.inventory as pinv

        pass # end of Inventory


    def _defaults(self):
        from LauncherMPICH2 import LauncherMPICH2
        self.inventory.launcher = LauncherMPICH2()
        return


    pass # end of Application

    

# version
__id__ = "$Id$"

# End of file 
