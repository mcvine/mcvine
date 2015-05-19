# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import os
debug = os.environ.get('DEBUG', False)


# paths
dvdir = os.environ.get('DV_DIR')
exportroot = os.environ.get('EXPORT_ROOT')
pyredir = os.environ.get("PYRE_DIR")
mcvinedir = os.environ.get("MCVINE_DIR")
mcvine_resources = os.environ.get("MCVINE_RESOURCES")

if dvdir and exportroot: type = 'developer'
else: 
    type = 'user'
    mcvinedir = mcvinedir or pyredir or exportroot
    if not mcvinedir:
        raise RuntimeError, "environment variable MCVINE_DIR was not defined. please define it to the path of the mcvine installation"


if mcvine_resources:
    mcvine_resources = os.path.abspath(mcvine_resources)


# version
__id__ = "$Id: __init__.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
