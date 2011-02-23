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

PROJECT = vitess
PACKAGE = pyre_components


RECURSE_DIRS = \

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
	Registry.py \
	Vitess.py \
	__init__.py \
	repositories.py \
	vitess.py \


EXPORT_BINS = \

export:: export-package-python-modules

# version
# $Id$
