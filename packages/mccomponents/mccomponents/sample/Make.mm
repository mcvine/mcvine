# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = mccomponents
PACKAGE = sample


BUILD_DIRS = \
	bindings \
	diffraction \
	idf \
	kernelxml \
	phonon \
	sansmodel \

RECURSE_DIRS = $(BUILD_DIRS)

#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse



#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	AbstractSQE.py \
	Broadened_E_Q_Kernel.py \
	ComputationEngineRendererExtension.py \
	ConstantEnergyTransferKernel.py \
	ConstantQEKernel.py \
	ConstantvQEKernel.py \
	E_Q_Kernel.py \
	E_vQ_Kernel.py \
	GridSQE.py \
	SQE_fromexpression.py \
	IsotropicKernel.py \
	KernelContainer.py \
	SQEkernel.py \
	__init__.py \
	sampleassembly_support.py \
	units.py \


export:: export-package-python-modules 
	BLD_ACTION="export" $(MM) recurse


#include doxygen/default.def
#docs: export-doxygen-docs


# version
# $Id$

# End of file
