# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = mccomponents
PACKAGE = bin


PROJ_LIBRARIES = -L$(BLD_LIBDIR) -lhistogram -ljournal -lmccomponents


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




events2iqe: events2iqe.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ events2iqe.cc


PROJ_CPPEXE = \
	events2iqe \


EXPORT_PYAPPS = \


EXPORT_BINS = $(PROJ_CPPEXE) $(EXPORT_PYAPPS)

export-binaries:: $(EXPORT_BINS)

export:: export-binaries release-binaries #export-package-python-modules 


# version
# $Id$

# End of file
