#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import os

from mcvine.deployment_info import mcvinedir, type

component_library_dir = os.environ.get('MCSTAS_COMPONENT_LIBDIR', None)
if component_library_dir is None:
    candidates = [
        os.path.join(mcvinedir, 'share', 'mcstas2', 'McStas-Components'),
        os.path.join(mcvinedir, 'share', 'mcvine', 'mcstas2', 'McStas-Components'),
        ]
    for c in candidates:
        if os.path.exists(c):
            component_library_dir = c
            break
        continue
    if not component_library_dir or not os.path.exists(component_library_dir):
        raise RuntimeError("Cannot find McStas component library in %s" % (candidates,))
        

    
# version
__id__ = "$Id$"

# End of file 
