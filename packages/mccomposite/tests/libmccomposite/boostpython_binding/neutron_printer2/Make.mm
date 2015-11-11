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
MODULE = neutron_printer2bp
PACKAGE = neutron_printer2bpmodule

include std-pythonmodule.def
include local.def


PROJ_CXX_SRCLIB = -lboost_python  -L$(BOOSTPYTHON_LIBDIR) \
	-ljournal -lmcni -lmccomposite \
	-L$(DANSE_DIR)/lib -L$(DANSE_DIR)/lib64


PROJ_SRCS = \
	wrap.cc \


EXPORT_PYTHON_MODULES = \
	neutron_printer2.py \


export:: export-python-modules 

include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id$

# End of file
