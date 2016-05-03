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
mcvine_workflow = os.environ.get('MCVINE_WORKFLOW')

if dvdir and exportroot: type = 'developer'
else: 
    type = 'user'
    mcvinedir = mcvinedir or pyredir or exportroot
    if not mcvinedir:
        danse_dir = os.environ.get("DANSE_DIR")
        if not danse_dir:
            raise RuntimeError, "Neither environment variable MCVINE_DIR nor DANSE_DIR was not defined. please define it to the path of the mcvine/danse installation"
        mcvinedir = danse_dir

if mcvine_resources:
    mcvine_resources = os.path.abspath(mcvine_resources)

# default location of mcvine workflow
if not mcvine_workflow:
    mcvine_workflow = os.path.join(mcvinedir, 'share', 'mcvine', 'workflow')

# End of file 
