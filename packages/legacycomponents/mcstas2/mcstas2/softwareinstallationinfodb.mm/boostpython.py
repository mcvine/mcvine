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


from Info import Info
from os import environ
libdir = environ['BOOSTPYTHON_LIBDIR']
incdir = environ['BOOSTPYTHON_INCDIR']

info = Info( include = incdir, lib = libdir ) # for mm, config is not necessary


# version
__id__ = "$Id$"

# End of file 
