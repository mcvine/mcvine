# -*- Makefile -*-

PROJECT = mcvineui

# directory structure

RECURSE_DIRS = \
	bin \
	cgi-bin \
	log \
	content \
	html \
	mcvineui \
	config



#--------------------------------------------------------------------------
#

all: 
	BLD_ACTION="all" $(MM) recurse

