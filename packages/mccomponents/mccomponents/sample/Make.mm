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
	idf \
	kernelxml \
	phonon \

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
	__init__.py \
	register_GridSQE.py \
	register_SQEkernel.py \
	register_KernelContainer.py \
	sampleassembly_support.py \
	units.py \


export:: export-package-python-modules 
	BLD_ACTION="export" $(MM) recurse


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id: Make.mm 1404 2007-08-29 15:43:42Z linjiao $

# End of file
