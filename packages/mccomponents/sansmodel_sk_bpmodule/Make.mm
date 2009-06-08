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

PROJECT = mccomponents
MODULE = sansmodel_sk_bp
PACKAGE = sansmodel_sk_bpmodule

include std-pythonmodule.def
include local.def


PROJ_CXX_SRCLIB = -lboost_python  -L$(BOOSTPYTHON_LIBDIR) -ljournal -lmccomposite -lmcni -lmcstas_compact -lmccomponents -lsansigor -lsansmodels


PROJ_SRCS = \
	wrap_sphere.cc \
	wrap_core_shell.cc \


TOUCH=touch

#wrap_basic_containers.cc: wrap_vector.h
#	$(TOUCH) wrap_basic_containers.cc


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id: Make.mm 658 2007-10-24 21:33:08Z linjiao $

# End of file

