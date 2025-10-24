# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

include local.def

PROJECT = bpext
PACKAGE = libbpext

PROJ_SAR = $(BLD_LIBDIR)/$(PACKAGE).$(EXT_SAR)
PROJ_DLL = $(BLD_BINDIR)/$(PACKAGE).$(EXT_SO)
PROJ_TMPDIR = $(BLD_TMPDIR)/$(PROJECT)/$(PACKAGE)
PROJ_CLEAN += $(PROJ_SAR) $(PROJ_DLL)

PROJ_SRCS = \
	extractor_registry.cc \
	wrapper_registry.cc \


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# build the library

all: $(PROJ_SAR) export release-headers

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
	bpext.h \
	extractor_registry.h \
	wrapper_registry.h \
	extract_ptr.h \
	wrap_ptr.h \
	WrappedPointer.h \

EXPORT_LIBS = $(PROJ_SAR)
EXPORT_BINS = $(PROJ_DLL)


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id: Make.mm 26 2007-05-16 13:52:10Z linjiao $

#
# End of file
