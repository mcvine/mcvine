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
MODULE = mccomponents
PACKAGE = mccomponentsbpmodule

include std-pythonmodule.def
include local.def


PROJ_CXX_SRCLIB = -lboost_python  -L$(BOOSTPYTHON_LIBDIR) -ljournal -lmccomposite -lmcni -lmcstas_compact -lmccomponents


PROJ_SRCS = \
	wrap_HomogeneousNeutronScatterer.cc \
	wrap_AbstractScatteringKernel.cc \
	wrap_CompositeScatteringKernel.cc \
	wrap_kernelcontainer.cc \


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id: Make.mm 658 2007-10-24 21:33:08Z linjiao $

# End of file
