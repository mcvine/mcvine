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

PROJECT = mcni
MODULE = mcni
PACKAGE = mcnibpmodule

include std-pythonmodule.def
include local.def


PROJ_CXX_SRCLIB = -lboost_python  -L$(BOOSTPYTHON_LIBDIR) -lmcni \
	-L$(DANSE_DIR)/lib -L$(DANSE_DIR)/lib64


PROJ_SRCS = \
	wrap_Vector3.cc \
	wrap_Matrix3.cc \
	wrap_geometry.cc \
	wrap_neutron.cc \
	wrap_abstractneutronscatterer.cc \
	wrap_abstractneutroncomponent.cc \
	wrap_dummycomponent.cc \


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id$

# End of file
