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

PROJECT = mccomposite
MODULE = mccomposite
PACKAGE = mccompositebpmodule

include std-pythonmodule.def
include local.def


PROJ_CXX_SRCLIB = -lboost_python  -L$(BOOSTPYTHON_LIBDIR) -ljournal -lmccomposite -lmcni 


PROJ_SRCS = \
	wrap_basics.cc \
	wrap_AbstractShape.cc \
	wrap_shapecontainer.cc \
	wrap_geometers.cc \
	wrap_primitives.cc \
	wrap_operations.cc \
	wrap_scatterercontainer.cc \
	wrap_shapeoperators.cc \
	wrap_AbstractNeutronScatterer.cc \
	wrap_CompositeNeutronScatterer.cc \


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id$

# End of file
