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


'''
Qgridinfo should contain python codes to give varaibles b1, b2, b3 and n1, n2, n3

b1, b2, b3 defines the reciprocal unit cell in which the grid is defined
n1, n2, n3 are number of points along directions of b1, b2, b3 respectively
'''

def read( path ):
    with open(path) as stream:
        lines = stream.readlines()
    d = locals()
    for line in lines:
        exec(line, d)
        continue
    return (d['b1'],d['b2'],d['b3']), (d['n1'],d['n2'],d['n3'])


# version
__id__ = "$Id$"

# End of file 
