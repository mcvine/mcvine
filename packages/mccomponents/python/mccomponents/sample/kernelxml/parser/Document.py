#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

from mccomponents.homogeneous_scatterer.hsxml.parser.Document import Document as base


class Document(base):

    tags = [
        'HomogeneousScatterer',
        'KernelContainer',

        'SQEkernel', 'GridSQE', 'SQE_fromexpression',
        'SQE_EnergyFocusing_Kernel',
        'SQkernel', 'GridSQ', 'SQ_fromexpression',
        'SvQkernel', 'GridSvQ', # 'SvQ_fromexpression',
        'ConstantEnergyTransferKernel',
        'ConstantQEKernel', 'ConstantvQEKernel',
        'E_Q_Kernel',
        'Broadened_E_Q_Kernel', 'LorentzianBroadened_E_Q_Kernel',
        'E_vQ_Kernel',

        'IsotropicKernel',
        'DGSSXResKernel',
        ]

    pass # end of Document

# version
__id__ = "$Id$"

# End of file 
