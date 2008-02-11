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


from sys import version_info
if version_info[0] <=2 and version_info[1] <= 3:
    def uniquelist( l ):
        u = {}
        for i in l: u[i] = 1
        return u.keys()
    
else:
    def uniquelist( l ):
        return [ u for u in l if u not in locals()['_[1]'] ]

del version_info



# version
__id__ = "$Id$"

# End of file 
