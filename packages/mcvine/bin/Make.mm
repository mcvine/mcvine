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

PROJECT = mcvine
PACKAGE = bin

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
	mcvine \
	mcvine-check-iqe \
	mcvine-check-angular-distribution \
	mcvine-create-instrument-simulation-application \
	mcvine-compare-pyre-registry \
	mcvine-compile-mcstas-component \
	mcvine-component-info \
	mcvine-list-components \
	mcvine-simulate \
	mcvine-neutron-storage-count-neutrons \
	mcvine-neutron-storage-extract \
	mcvine-neutron-storage-merge \
	mcvine-neutron-storage-get-neutrons \
	mcvine-neutron-storage-print-neutrons \
	mcvine-neutron-storage-total-intensity \
	mcvine-reduce-eventdata-to-ipix \
	mcvine-reduce-eventdata-to-ipixtof \
	mcvine-reduce-eventdata-to-itof \
	mcvine-simulation-get-progress \
	mcvine-spe2sqehist \


export:: export-binaries release-binaries export-package-python-modules #export-docs


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id$

# End of file
