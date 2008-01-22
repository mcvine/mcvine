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


## create local.def


template = '''
PROJ_CXX_INCLUDES += %(includes_str)s
'''


class Generator:

    target = 'local.def'

    def __init__(self, includes = []):
        self.includes = includes
        return
    
    def generate(self, path, target = None ):
        if not target: target = self.target
        
        includes_str = ' '.join( self.includes )
        content = template % {
            'includes_str' : includes_str,
            }
        import os
        filename = os.path.join( path, target )

        open(filename, 'w').write( content )
        return filename

    pass # end of Generate
    

# version
__id__ = "$Id$"

# End of file 
