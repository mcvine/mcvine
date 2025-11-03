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

PROJECT = bpext
MODULE = _examplebpbinding
PACKAGE = _examplebpbindingmodule

include std-pythonmodule.def
include local.def

PROJ_CXX_SRCLIB = -lboost_python -L$(BOOSTPYTHON_LIBDIR) 


PROJ_SRCS = \
	wrap.cc \


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id: Make.mm 619 2007-05-15 04:25:25Z linjiao $

# End of file
