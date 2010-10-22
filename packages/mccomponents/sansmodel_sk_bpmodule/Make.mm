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


PROJ_CXX_SRCLIB = -lboost_python  -L$(BOOSTPYTHON_LIBDIR) -ljournal -lmccomposite -lmcni -lmccomponents -lsansigor -lsansmodels


PROJ_SRCS = \
	wrap_cylinder.cc \
	wrap_ellipsoid.cc \
	wrap_elliptical_cylinder.cc \
	wrap_sphere.cc \
	wrap_core_shell.cc \
	wrap_core_shell_cylinder.cc \


TOUCH=touch

#wrap_basic_containers.cc: wrap_vector.h
#	$(TOUCH) wrap_basic_containers.cc


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id$

# End of file

