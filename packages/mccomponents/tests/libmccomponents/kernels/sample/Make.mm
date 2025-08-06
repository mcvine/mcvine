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


# local tests
PROJ_TIDY += $(PROJ_CPPTESTS)
PROJ_CLEAN += $(PROJ_CPPTESTS)
PROJ_PYTESTS =  #alltests.py
PROJ_CPPTESTS = \
	test_Broadened_E_Q_Kernel \
	test_E_Q_Kernel \
	test_E_vQ_Kernel \
	test_SQkernel \
	test_SQAdaptor \
	test_SQE_fromexpression \
	test_SvQ_fromexpression \


PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)

PROJ_CXX_INCLUDES += $(DANSE_DIR)/include $(DANSE_DIR)/include/danse/ins
# PROJ_LIBRARIES = -L$(BLD_LIBDIR) -lmcni -lmccomposite -lmccomponents -lfparser
PROJ_LIBRARIES = -L$(BLD_LIBDIR) \
	-lmccomponents -lmccomposite -lmcni \
	-lfparser \
	-lgsl -lgslcblas -L$(GSL_LIBDIR) \
	-L$(DANSE_DIR)/lib -L$(DANSE_DIR)/lib64
# PROJ_CXX_DEFINES += DEEPDEBUG


# for recursion
# directory structure

BUILD_DIRS = \
	diffraction \
	phonon \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
# build the library
all: $(PROJ_TESTS)
	BLD_ACTION="all" $(MM) recurse

test: 
	BLD_ACTION="test" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

#--------------------------------------------------------------------------




test_SQkernel: test_SQkernel.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_SQkernel.cc $(PROJ_LIBRARIES)

test_SQAdaptor: test_SQAdaptor.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_SQAdaptor.cc $(PROJ_LIBRARIES)

test_SQE_fromexpression: test_SQE_fromexpression.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_SQE_fromexpression.cc $(PROJ_LIBRARIES)

test_SvQ_fromexpression: test_SvQ_fromexpression.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_SvQ_fromexpression.cc $(PROJ_LIBRARIES)

test_Broadened_E_Q_Kernel: test_Broadened_E_Q_Kernel.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_Broadened_E_Q_Kernel.cc $(PROJ_LIBRARIES)

test_E_Q_Kernel: test_E_Q_Kernel.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_E_Q_Kernel.cc $(PROJ_LIBRARIES)

test_E_vQ_Kernel: test_E_vQ_Kernel.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_E_vQ_Kernel.cc $(PROJ_LIBRARIES)



# version
# $Id$

#
# End of file

