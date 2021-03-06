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
	AbstractNeutronScatterer.cc \
	CompositeNeutronScatterer.cc \
	CompositeNeutronScatterer_Impl.cc \
	Arrow.cc \
	ArrowIntersector.cc \
	Box.cc \
	Cylinder.cc \
	Locator.cc \
	Sphere.cc \
	Printer.cc \
	intersect.cc \
	locate.cc \
	neutron_propagation.cc \
	shape2ostream.cc \


PROJ_TIDY += $(PROJ_SRCS)


AbstractNeutronScatterer.cc: ../mccomposite/AbstractNeutronScatterer.cc
	cp ../mccomposite/AbstractNeutronScatterer.cc .

CompositeNeutronScatterer.cc: ../mccomposite/CompositeNeutronScatterer.cc
	cp ../mccomposite/CompositeNeutronScatterer.cc .

CompositeNeutronScatterer_Impl.cc: ../mccomposite/CompositeNeutronScatterer_Impl.cc
	cp ../mccomposite/CompositeNeutronScatterer_Impl.cc .

Arrow.cc: ../geometry/visitors/Arrow.cc
	cp ../geometry/visitors/Arrow.cc .

ArrowIntersector.cc: ../geometry/visitors/ArrowIntersector.cc
	cp ../geometry/visitors/ArrowIntersector.cc .

Box.cc: ../geometry/primitives/Box.cc
	cp ../geometry/primitives/Box.cc .

Cylinder.cc: ../geometry/primitives/Cylinder.cc
	cp ../geometry/primitives/Cylinder.cc .

Sphere.cc: ../geometry/primitives/Sphere.cc
	cp ../geometry/primitives/Sphere.cc .

Locator.cc: ../geometry/visitors/Locator.cc
	cp ../geometry/visitors/Locator.cc .

Printer.cc: ../geometry/visitors/Printer.cc
	cp ../geometry/visitors/Printer.cc .

intersect.cc: ../geometry/intersect.cc
	cp ../geometry/intersect.cc .

locate.cc: ../geometry/locate.cc
	cp ../geometry/locate.cc .

shape2ostream.cc: ../geometry/shape2ostream.cc
	cp ../geometry/shape2ostream.cc .

neutron_propagation.cc: ../mccomposite/neutron_propagation.cc
	cp ../mccomposite/neutron_propagation.cc .



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

