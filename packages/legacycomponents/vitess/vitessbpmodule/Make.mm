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

PROJECT = vitess
MODULE = vitess
PACKAGE = vitessbpmodule

include std-pythonmodule.def
include local.def


PROJ_CXX_SRCLIB = -lboost_python  -L$(BOOSTPYTHON_LIBDIR) -ljournal -lmcni -lvitess


PROJ_SRCS = \
	wrap_converters.cc \


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id$

# End of file
