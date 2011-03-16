# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2008  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = mcvine
PACKAGE = sphinx


EXPORT_DATADIRS = \
	tutorials \
	examples \


RECURSE_DIRS = \


#--------------------------------------------------------------------------
#

all: docs
	BLD_ACTION="all" $(MM) recurse

PROJ_CLEAN = \
	_build/* \

clean:: sphinx-clean
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

docs: jsmath sphinx-build export-sphinx-data


jsmath::
	if [ -z $(JSMATH_DIR) ]; \
	then \
	  echo Please define env var JSMATH_DIR to point to the directory of jsmath; \
	  exit 1;\
	else \
	  rsync -a $(JSMATH_DIR)/ _static/jsmath/ ;\
	fi; \


EXPORT_DATADIRS = \
	_static/jsmath \

include std-docs.def
include sphinx/default.def


# version
# $Id$

# End of file
