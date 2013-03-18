#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import numpy as np


class ParabolicFittingError(Exception): pass
def fitparabolic(E, g, N=100, minN = 20):
    """fit the near zero portion of the dos curve to parabolic
    """
    def fit(N):
        E1 = E[:N]; g1 = g[:N]
        return linear_regression(E1*E1, g1)
    badfit = True
    while N > minN:
        c, R2 = fit(N)
        if R2 < 0.9: N-=1
        else: badfit = False; break
        continue
    if badfit:
        # import pylab; pylab.plot(E, g); pylab.show()
        raise ParabolicFittingError("Unable to fit DOS to parabolic")
    E1 = E[:N]
    g[:N] = c * E1*E1
    return E,g
    

def linear_regression(x,y):
    """ fit y = cx. return c and R**2
    """
    c = (x*y).sum() / (x*x).sum()
    y_ave = np.average(y)
    SS_tot = ((y - y_ave)**2).sum()
    SS_err = ((y - c*x)**2).sum()
    R2 = 1-SS_err/SS_tot
    return c, R2


# version
__id__ = "$Id$"

# End of file 
