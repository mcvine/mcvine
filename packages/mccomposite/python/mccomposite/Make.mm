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
	coordinate_systems \
	geometry  \
	bindings \
	orientation_conventions \
	extensions \

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
	ScattererComputationEngineRenderer.py \
	ScattererComputationEngineFactory.py \
	Geometer.py \
	McStasConvention.py \
	Scatterer.py \
	ScattererCopy.py \
	__init__.py \
	units.py \
	units_utils.py \


export:: export-python-modules 
	BLD_ACTION="export" $(MM) recurse


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id$

# End of file
