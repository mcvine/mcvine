#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from mccomponents.homogeneous_scatterer.hsxml.parser.HomogeneousScatterer import HomogeneousScatterer as base

class HomogeneousScatterer( base ):

    onConstantQEKernel = onConstantvQEKernel = base.onKernel
    onConstantEnergyTransferKernel = base.onKernel
    onBroadened_E_Q_Kernel = onE_Q_Kernel = onE_vQ_Kernel = base.onKernel
    onSQEkernel = onSQkernel = onSvQkernel = base.onKernel
    onSQE_EnergyFocusing_Kernel = base.onKernel
    onIsotropicKernel = base.onKernel
    onDGSSXResKernel = base.onKernel


# version
__id__ = "$Id$"

# End of file 
