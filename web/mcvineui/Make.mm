# -*- Makefile -*-

PROJECT = mcvineui

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	__init__.py



export:: export-python-modules
