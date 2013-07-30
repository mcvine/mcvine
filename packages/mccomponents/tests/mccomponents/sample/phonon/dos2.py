#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2013 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def loadDOS():
    f = 'V-DOS.idf'
    from mccomponents.sample.idf import readDOS
    e, Z = readDOS(f)
    de = e[1] - e[0]
    Z /= Z.sum() * de
    return e,Z
    

# version
__id__ = "$Id$"

# End of file 
