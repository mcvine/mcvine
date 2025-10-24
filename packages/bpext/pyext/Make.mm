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
PACKAGE = _bpextmodule
MODULE = _bpext

include std-pythonmodule.def
include local.def

PROJ_CXX_SRCLIB = -lbpext -lboost_python  -L$(BOOSTPYTHON_LIBDIR) -ljournal
#-lscitbx_boost_python -L$(BOOSTPYTHON_LIBDIR)

ifeq (Win32, ${findstring Win32, $(PLATFORM_ID)})

  PROJ_CXX_SRCLIB = -L$(BOOSTPYTHON_LIBDIR)  -lboost_python        

endif


PROJ_SRCS = \
	bindings.cc \
	dblarr.cc \
	exceptions.cc \
	misc.cc \
	register_converters.cc \


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id: Make.mm 26 2007-05-16 13:52:10Z linjiao $

# End of file
