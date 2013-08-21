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

PROJECT = mcvine

BUILD_DIRS = \
	applications \
	cli \
	instrument \
	instruments \
	pyre_support \
	scripts \


RECURSE_DIRS = $(BUILD_DIRS)

PACKAGE = mcvine

PROJ_TIDY += svn-commit*.tmp

#--------------------------------------------------------------------------
#

all: export

tidy::
	BLD_ACTION="tidy" $(MM) recurse



#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	component_suppliers.py \
	deployment_info.py \
	__init__.py \


export:: export-python-modules 
	BLD_ACTION="export" $(MM) recurse


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id$

# End of file
