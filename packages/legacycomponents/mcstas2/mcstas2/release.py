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

from mcvine.development_info import mcvinedir

component_library_dir = os.environ.get('MCSTAS_COMPONENT_LIBDIR', None)
if component_library_dir is None:
    component_library_dir = os.path.join(mcvinedir, 'share', 'mcstas2', 'McStas-Components')

    
# version
__id__ = "$Id$"

# End of file 
