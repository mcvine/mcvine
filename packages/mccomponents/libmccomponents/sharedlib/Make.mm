# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

include local.def

PROJECT = mccomponents
PACKAGE = libmccomponents


# library
PROJ_SAR = $(BLD_LIBDIR)/$(PACKAGE).$(EXT_SAR)
PROJ_DLL = $(BLD_BINDIR)/$(PACKAGE).$(EXT_SO)
PROJ_TMPDIR = $(BLD_TMPDIR)/$(PROJECT)/$(PACKAGE)
PROJ_CLEAN += $(PROJ_SAR) $(PROJ_DLL)


#--------------------------------------------------------------------------
# build the library
all: $(PROJ_SAR) export

#--------------------------------------------------------------------------


PROJ_SRCS = \
	HomogeneousNeutronScatterer.cc \
	random.cc \
	CompositeScatteringKernel.cc \
	EventModeMCA.cc \
	He3.cc \
	He3Tube.cc \


PROJ_TIDY += $(PROJ_SRCS)


HomogeneousNeutronScatterer.cc: ../homogeneous_scatterer/HomogeneousNeutronScatterer.cc
	cp ../homogeneous_scatterer/HomogeneousNeutronScatterer.cc .

random.cc: ../math/random.cc
	cp ../math/random.cc .

CompositeScatteringKernel.cc: ../homogeneous_scatterer/CompositeScatteringKernel.cc
	cp ../homogeneous_scatterer/CompositeScatteringKernel.cc .

He3.cc: ../kernels/detector/He3.cc
	cp ../kernels/detector/He3.cc .

He3Tube.cc: ../kernels/detector/He3Tube.cc
	cp ../kernels/detector/He3Tube.cc .

EventModeMCA.cc: ../kernels/detector/EventModeMCA.cc
	cp ../kernels/detector/EventModeMCA.cc .



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ifeq (Win32, ${findstring Win32, $(PLATFORM_ID)})

# build the shared object
$(PROJ_SAR): product_dirs $(PROJ_OBJS)
	$(CXX) $(LCXXFLAGS) -o $(PROJ_DLL) \
	-Wl,--out-implib=$(PROJ_SAR) $(PROJ_OBJS)

# export
export:: export-headers export-libraries export-binaries

else

# build the shared object
$(PROJ_SAR): product_dirs $(PROJ_OBJS)
	$(CXX) $(LCXXFLAGS) -o $(PROJ_SAR) $(PROJ_OBJS)

# export
export:: export-headers export-libraries

endif

EXPORT_HEADERS = \


EXPORT_LIBS = $(PROJ_SAR)
EXPORT_BINS = $(PROJ_DLL)


# version
# $Id$

#
# End of file

