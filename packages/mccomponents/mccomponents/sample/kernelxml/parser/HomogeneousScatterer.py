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

    onConstantQEKernel = onConstantEnergyTransferKernel = base.onKernel
    onSQEkernel = base.onKernel
    onIsotropicKernel = base.onKernel


# version
__id__ = "$Id: __init__.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
