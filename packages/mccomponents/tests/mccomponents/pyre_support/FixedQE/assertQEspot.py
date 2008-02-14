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


# after reduction the S(Q,E) should only have one bright spot at (5, 30)


import pickle


sqe = pickle.load( open('reduction/sqehist.pkl') )
qaxis = sqe.axisFromName( 'Q' )
eaxis = sqe.axisFromName( 'energy' )

qs = qaxis.binCenters()
es = eaxis.binCenters()


from sim_params import Q,E

for q in qs:
    for e in es:
        s = sqe[q,e][0]
        #right on spot. must be positive
        if q == Q and e == E : assert s > 0; continue
        #neighbors, not sure
        if abs(q-Q)/Q < 0.05 and abs(e-E)/E < 0.05: continue
        #others, must be zero
        assert s == 0, 'q=%s, e=%s, s=%s' % (q,e, s)
        continue
    continue

    
# version
__id__ = "$Id$"

# End of file 

