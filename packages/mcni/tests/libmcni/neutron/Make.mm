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

PROJECT = simulation
PACKAGE = tests

PROJ_TIDY += $(PROJ_CPPTESTS)
PROJ_CLEAN += $(PROJ_CPPTESTS)

PROJ_PYTESTS =  alltests.py
PROJ_CPPTESTS = testEvent testCeventbuffer testcoords_transform testunits_conversion
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_CXX_INCLUDES += $(DANSE_DIR)/include $(DANSE_DIR)/include/danse/ins
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -lmcni \
	-L$(DANSE_DIR)/lib -L$(DANSE_DIR)/lib64


#--------------------------------------------------------------------------
#

all: $(PROJ_TESTS)

test:
	for test in $(PROJ_TESTS) ; do $${test}; done

release: tidy
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#

testCeventbuffer: testCeventbuffer.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testCeventbuffer.cc $(PROJ_LIBRARIES)

testEvent: testEvent.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testEvent.cc $(PROJ_LIBRARIES)

testcoords_transform: testcoords_transform.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testcoords_transform.cc $(PROJ_LIBRARIES)

testunits_conversion: testunits_conversion.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testunits_conversion.cc $(PROJ_LIBRARIES)


# version
# $Id$

# End of file
