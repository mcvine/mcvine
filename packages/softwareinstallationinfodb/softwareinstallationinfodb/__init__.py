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

## This is a template.
## softwareinstallationinfodb package should be exported as a "root" python
## package.
## It must provide one method to return info of a software installation.
## The installation info instance must have following attributes:
##   - root: path to the root of the installation path
##   - bin: path containing executables
##   - include: path containing headers
##   - lib: path containing shared libraries

def info( name ): raise NotImplementedError


# version
__id__ = "$Id$"

# End of file 
