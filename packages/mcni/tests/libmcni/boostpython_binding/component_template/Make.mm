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

PROJECT = xxxPROJECTxxx
MODULE = xxxMODULExxxbp
PACKAGE = xxxMODULExxxbpmodule

include std-pythonmodule.def
include local.def


PROJ_CXX_SRCLIB = -lboost_python  -L$(BOOSTPYTHON_LIBDIR) -lmcni


PROJ_SRCS = \
	wrap.cc \


EXPORT_PYTHON_MODULES = \
	xxxMODULExxx.py

export:: export-python-modules 


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id$

# End of file
