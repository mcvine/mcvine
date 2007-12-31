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

PROJECT = mccomposite

BUILD_DIRS = \
	geometry  \
	bindings \

RECURSE_DIRS = $(BUILD_DIRS)

PACKAGE = mccomposite

#--------------------------------------------------------------------------
#

all: export

tidy::
	BLD_ACTION="tidy" $(MM) recurse



#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	AbstractBinding.py \
	AbstractOrientationConvention.py \
	AbstractVisitor.py \
	CompositeScatterer.py \
	ComputingEngineConstructor.py \
	Geometer.py \
	McStasConvention.py \
	Scatterer.py \
	ScattererComputingEngineFactory.py \
	__init__.py \


export:: export-python-modules 
	BLD_ACTION="export" $(MM) recurse


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id: Make.mm 1404 2007-08-29 15:43:42Z linjiao $

# End of file
