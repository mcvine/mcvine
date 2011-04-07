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


from mccomponents.homogeneous_scatterer.hsxml.parser.Document import Document as base


class Document(base):


    tags = [
        'HomogeneousScatterer',
        'KernelContainer',

        'SQEkernel',
        'GridSQE',
        'SQE_fromexpression',
        'ConstantEnergyTransferKernel',
        'ConstantQEKernel',
        'E_Q_Kernel',

        'IsotropicKernel',
        ]


    pass # end of Document

# version
__id__ = "$Id$"

# End of file 
