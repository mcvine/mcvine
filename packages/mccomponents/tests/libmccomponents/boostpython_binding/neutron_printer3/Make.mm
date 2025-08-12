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
#

PROJECT = 
MODULE = neutron_printer3bp
PACKAGE = neutron_printer3bpmodule

include std-pythonmodule.def
include local.def


PROJ_CXX_INCLUDES += $(DANSE_DIR)/include $(DANSE_DIR)/include/danse/ins
PROJ_CXX_SRCLIB = \
	-lboost_python -L$(BOOSTPYTHON_LIBDIR) \
	-lmccomponents -lmccomposite -lmcni \
	-L$(DANSE_DIR)/lib -L$(DANSE_DIR)/lib64

PROJ_SRCS = \
	wrap.cc \


EXPORT_PYTHON_MODULES = \
	neutron_printer3.py \


export:: export-python-modules 

include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id$

# End of file
