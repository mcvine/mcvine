#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp



def example():
    vector = mccomponentsbp.vector_double
    Z = vector( 50 )
    area = 0
    for i in range(50):
        Z[i] = i*i
        area += Z[i]
        continue
    dos = mccomponentsbp.LinearlyInterpolatedDOS_dbl(
        0, 1., 50, Z )
    
    dw = mccomponentsbp.DWFromDOS_dbl(
        dos, 100 )
    mass = 50
    temperature = 300
    dw.calc_DW_core( mass, temperature )
    return dw


# version
__id__ = "$Id$"

# End of file 
