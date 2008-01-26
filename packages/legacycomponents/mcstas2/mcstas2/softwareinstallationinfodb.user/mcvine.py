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
from os.path import join
root = environ['MCVINE']
incdir = join( root, 'include' )
libdir = join( root, 'lib' )
etc = join( root, 'etc' )
python = join( root, 'modules' )

info = Info( root = root, include = incdir, lib = libdir, etc = etc ) 


# version
__id__ = "$Id$"

# End of file 
