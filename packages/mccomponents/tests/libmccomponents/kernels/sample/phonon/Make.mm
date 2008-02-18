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


PROJECT = mccomponents/tests
PACKAGE = libmccomponents/kernels


PROJ_TIDY += $(PROJ_CPPTESTS)
PROJ_CLEAN += $(PROJ_CPPTESTS)

PROJ_PYTESTS =  #alltests.py
PROJ_CPPTESTS = test_LinearlyInterpolatedGridData_3D \
	test_LinearlyInterpolatedPolarizationOnGrid_3D \
	test_LinearlyInterpolatedDispersionOnGrid_3D \
	test_LinearlyInterpolatedGridData_1D \
	test_LinearlyInterpolatedDOS \
	test_CoherentInelastic_PolyXtal \


PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -ljournal -lmcni -lmccomposite -lmccomponents
PROJ_CXX_DEFINES += DEEPDEBUG


# directory structure

BUILD_DIRS = \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
# build the library
all: $(PROJ_TESTS)
	BLD_ACTION="all" $(MM) recurse

test: $(PROJ_TESTS)
	for test in $(PROJ_TESTS) ; do $${test}; done
	BLD_ACTION="test" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

#--------------------------------------------------------------------------



test_LinearlyInterpolatedGridData_1D: test_LinearlyInterpolatedGridData_1D.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_LinearlyInterpolatedGridData_1D.cc $(PROJ_LIBRARIES)

test_LinearlyInterpolatedDOS: test_LinearlyInterpolatedDOS.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_LinearlyInterpolatedDOS.cc $(PROJ_LIBRARIES)

test_LinearlyInterpolatedGridData_3D: test_LinearlyInterpolatedGridData_3D.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_LinearlyInterpolatedGridData_3D.cc $(PROJ_LIBRARIES)

test_LinearlyInterpolatedPolarizationOnGrid_3D: test_LinearlyInterpolatedPolarizationOnGrid_3D.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_LinearlyInterpolatedPolarizationOnGrid_3D.cc $(PROJ_LIBRARIES)

test_LinearlyInterpolatedDispersionOnGrid_3D: test_LinearlyInterpolatedDispersionOnGrid_3D.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_LinearlyInterpolatedDispersionOnGrid_3D.cc $(PROJ_LIBRARIES)

test_CoherentInelastic_PolyXtal: test_CoherentInelastic_PolyXtal.cc CoherentInelastic_PolyXtal_Example.h LinearlyInterpolatedDispersionOnGrid_3D_Example.h
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_CoherentInelastic_PolyXtal.cc $(PROJ_LIBRARIES)



# version
# $Id$

#
# End of file

