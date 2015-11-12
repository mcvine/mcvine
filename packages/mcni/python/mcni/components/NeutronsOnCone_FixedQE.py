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


category = 'sources'


from mcni.AbstractComponent import AbstractComponent


class NeutronsOnCone_FixedQE(AbstractComponent):

    ''' A source that emits neutrons in a cone that has
    fixed Q, E values. Q is momentum transfer, E is energy transfer.
    Incident neutron beams is assumed to be monochromatic
    and has energy Ei.
    The flight length from moderator to sample is L1.
    This is useful for testing detectors.
    '''

    def __init__(self, name, Q, E, Ei, L1):
        AbstractComponent.__init__(self, name)
        Ef = Ei - E
        
        from mcni.utils import e2k, e2v
        ki = e2k( Ei )
        kf = e2k( Ef )
        
        assert Q > abs(kf-ki) and Q < ki+kf, \
               'invalid: ki=%s, kf=%s, Q=%s' % (
            ki, kf, Q )
        
        cost = (ki*ki+kf*kf-Q*Q)/2/ki/kf

        from math import acos, cos, sin
        theta = acos( cost )

        vf = e2v( Ef )
        self.vz = vf * cos( theta )
        self.vp = vf * sin( theta )

        vi = e2v( Ei )
        self.t0 = L1/vi
        return


    def process(self, neutrons):
        from random import random
        from math import pi, sin, cos
        vp = self.vp
        vz = self.vz
        t0 = self.t0
        for i in range( len(neutrons) ):
            phi = random() * 2 * pi
            vx = vp * cos(phi)
            vy = vp * sin(phi)
            neutron = mcni.neutron(
                time = t0, prob = 1.0,
                r = (0,0,0), v = (vx,vy,vz) )
            neutrons[i] = neutron
            continue
        return neutrons
    
    pass # end of  NeutronsOnCone_FixedQE


import mcni



# version
__id__ = "$Id$"

# End of file 


