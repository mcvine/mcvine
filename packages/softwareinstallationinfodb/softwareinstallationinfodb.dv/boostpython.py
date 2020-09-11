#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .Info import Info
import os
libdir = os.environ.get('BOOSTPYTHON_LIBDIR')
incdir = os.environ.get('BOOSTPYTHON_INCDIR')

conda_prefix = os.environ.get('CONDA_PREFIX')
if conda_prefix:
    libdir = libdir or os.path.join(conda_prefix, 'lib')
    incdir = incdir or os.path.join(conda_prefix, 'include')

info = Info( include = incdir, lib = libdir ) # for mm, config is not necessary


# version
__id__ = "$Id$"

# End of file 
