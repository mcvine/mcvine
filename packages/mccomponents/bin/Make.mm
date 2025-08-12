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


PROJ_CXX_INCLUDES += $(DANSE_DIR)/include $(DANSE_DIR)/include/danse/ins
PROJ_LIBRARIES = -L$(BLD_LIBDIR) \
	-lhistogram -lmcni -lmccomposite -lmccomponents -lfparser \
	-L$(DANSE_DIR)/lib -L$(DANSE_DIR)/lib64
PROJ_CXX_DEFINES += USE_DANSE_NAMESPACE

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





PROJ_CPPEXE = \


EXPORT_PYAPPS = \
	mcvine-debye-waller-core-from-phonon-dos \


EXPORT_BINS = $(EXPORT_PYAPPS) $(PROJ_CPPEXE) 

export-binaries:: $(EXPORT_BINS)

export:: export-binaries release-binaries #export-package-python-modules 


# version
# $Id$

# End of file
