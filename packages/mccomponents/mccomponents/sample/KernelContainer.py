#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# KernelContainer is an alias of homogeneous_scatterer.CompositeKernel.CompositeKernel

from mccomponents.homogeneous_scatterer.CompositeKernel import CompositeKernel
KernelContainer = CompositeKernel


# 2. the handler for renderer
def onKernelContainer(self, kernelcontainer):
    return self.onCompositeKernel( kernelcontainer )

import mccomponents.homogeneous_scatterer as hs
# 4. register the new class and handlers
hs.register_engine_renderer_handler (
    KernelContainer, onKernelContainer )


# version
__id__ = "$Id$"

# End of file 
