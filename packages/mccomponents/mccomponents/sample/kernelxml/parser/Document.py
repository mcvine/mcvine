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

        'IsotropicKernel',
        ]


    pass # end of Document

# version
__id__ = "$Id: Document.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
