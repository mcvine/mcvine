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

PROJECT = mcni
PACKAGE = libmcni


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
	exception.cc \
	Vector3.cc \
	Event.cc \
	EventBuffer.cc \
	Spin.cc \
	State.cc \
	Ceventbuffer.cc \
	process_neutron_events.cc \


PROJ_TIDY += $(PROJ_SRCS)


exception.cc: ../test/exception.cc
	cp ../test/exception.cc .

Vector3.cc: ../geometry/Vector3.cc
	cp ../geometry/Vector3.cc .

Event.cc: ../neutron/Event.cc
	cp ../neutron/Event.cc .

EventBuffer.cc: ../neutron/EventBuffer.cc
	cp ../neutron/EventBuffer.cc .

Spin.cc: ../neutron/Spin.cc
	cp ../neutron/Spin.cc .

State.cc: ../neutron/State.cc
	cp ../neutron/State.cc .

Ceventbuffer.cc: ../neutron/Ceventbuffer.cc
	cp ../neutron/Ceventbuffer.cc .

process_neutron_events.cc: ../mcni/process_neutron_events.cc
	cp ../mcni/process_neutron_events.cc .


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
