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




V2K = 1.58801E-3 # Convert v[m/s] to k[1/AA]
K2V = 1./V2K
SE2V = 437.3949	   #/* Convert sqrt(E)[meV] to v[m/s] */
VS2E = 5.227e-6	   #/* Convert (v[m/s])**2 to E[meV] */
def v2k(vel):
    return V2K * vel
def e2v(energy):
    from numpy import sqrt
    return sqrt(energy)*SE2V
def e2k(energy):
    return v2k( e2v( energy) )
def k2v(k):
    return K2V * k
def v2e(v):
    return v*v*VS2E
def k2e(k):
    return v2e( k2v( k) )




# version
__id__ = "$Id$"

# End of file 
