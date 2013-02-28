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
    f = 'V-dos.dat'
    from mcni.utils.constants import hbar, e
    from math import pi
    # constant to convert frequency on terahertz to energy in meV
    toenergy = hbar * 1e12 * 2*pi / e * 1e3
    
    lines = open(f).readlines()
    es, Is = [], []
    for line  in lines:
        if line.startswith('#'): continue
        line = line.strip()
        e, I = line.split()
        es.append(float(e)*toenergy)
        Is.append(float(I))
        continue
    import histogram
    h = histogram.histogram(
        'dos', 
        [('energy', es, 'meV')],
        Is)
    return h
    

# version
__id__ = "$Id$"

# End of file 
