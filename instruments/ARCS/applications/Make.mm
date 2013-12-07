# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

PROJECT = mcvine/instruments/ARCS
PACKAGE = applications

# directory structure

BUILD_DIRS = \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)

#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse



EXPORT_PYTHON_MODULES = \


EXPORT_BINS = \
	arcs_analyze_beam \
	arcs_beam \
	arcs-compute-IQE-resolution \
	arcs-events2nxs \
	arcs-events2iqe-directly \
	arcs_moderator2sample \
	arcs-m2s \
	arcs-neutrons2events \
	arcs-neutrons2nxs \
	arcs-nxs-populate-monitordata \
	arcs-reduce-nxs-using-mantid \
	arcs-extract-iqe-from-nxs \


export:: export-binaries release-binaries export-package-python-modules #export-docs


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id$

# End of file
