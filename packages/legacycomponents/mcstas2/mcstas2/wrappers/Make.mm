PROJECT = mcstas2
PACKAGE = wrappers


RECURSE_DIRS = \
    component2cppClass \

#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
    __init__.py \

export:: export-package-python-modules

# version
# $Id: Make.mm 115 2004-09-22 22:29:06Z linjiao $
