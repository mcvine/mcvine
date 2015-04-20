# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                        California Institute of Technology
#                        (C) 2006-2011  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

PROJECT = mcvine
PACKAGE = docs/sphinx/examples

# directory structure

#--------------------------------------------------------------------------
all: export
#

clean:: clean-data
	BLD_ACTION="clean" $(MM) recurse


TMPDIR=$(BLD_ROOT)/tmp/$(PROJECT)/$(PACKAGE)
SPHINX_OUTPUT_DIR=$(EXPORT_ROOT)/docs/mcvine/sphinx
EXAMPLE_TARBALL=$(SPHINX_OUTPUT_DIR)/examples.tgz
REPO=svn://danse.us/MCViNE/trunk/docs/sphinx/examples

export:: export-package-data

# check out this examples directory to a temporary directory 
# remove .svn and Make.mm
# create tar ball
export-package-data:: 
	rm -rf $(TMPDIR) ; \
	mkdir -p $(TMPDIR) ; \
	cd $(TMPDIR) ; \
	svn co $(REPO) examples ; \
	find examples -name .svn -exec rm -rf {} \; ; \
	find examples -name Make.mm -exec rm -f {} \; ; \
	mkdir -p $(SPHINX_OUTPUT_DIR); \
	tar czf $(EXAMPLE_TARBALL) examples ; \


clean-data::
	find . -name out -exec rm -rf {} \; ; \
	find . -name *.dat -exec rm -rf {} \; ; \
	find . -name *.pml.* -exec rm -rf {} \; 

# version
# $Id$

# End of file
