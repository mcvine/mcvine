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

PROJECT = mccomposite
PACKAGE = libmccomposite


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
	Arrow.cc \
	ArrowIntersector.cc \
	Box.cc \
	Printer.cc \
	shape2ostream.cc \


PROJ_TIDY += $(PROJ_SRCS)


Arrow.cc: ../geometry/visitors/Arrow.cc
	cp ../geometry/visitors/Arrow.cc .

ArrowIntersector.cc: ../geometry/visitors/ArrowIntersector.cc
	cp ../geometry/visitors/ArrowIntersector.cc .

Box.cc: ../geometry/primitives/Box.cc
	cp ../geometry/primitives/Box.cc .

Printer.cc: ../geometry/visitors/Printer.cc
	cp ../geometry/visitors/Printer.cc .

shape2ostream.cc: ../geometry/shape2ostream.cc
	cp ../geometry/shape2ostream.cc .



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

