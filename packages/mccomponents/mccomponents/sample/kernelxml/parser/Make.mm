# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = mccomponents
PACKAGE = sample/kernelxml/parser

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	AbstractNode.py \
	Broadened_E_Q_Kernel.py \
	ConstantEnergyTransferKernel.py \
	ConstantQEKernel.py \
	Document.py \
	E_Q_Kernel.py \
	E_vQ_Kernel.py \
	GridSQE.py \
	SQE_fromexpression.py \
	HomogeneousScatterer.py \
	IsotropicKernel.py \
	KernelContainer.py \
	ScatteringKernel.py \
	SQEkernel.py \
	__init__.py \


#include doxygen/default.def

export:: export-package-python-modules 

# version
# $Id$

# End of file
