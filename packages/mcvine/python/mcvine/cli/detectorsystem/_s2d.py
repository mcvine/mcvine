# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, warnings, numpy as np
import mcvine, mcvine.components as mc

from mcni.pyre_support.AbstractComponent import AbstractComponent
class IsotropicSource( AbstractComponent ):

    def __init__(self, name, v):
        AbstractComponent.__init__(self, name=name)
        self.v = v
        return

    def process(self, neutrons):
        if not len(neutrons): return
        N = len(neutrons)
        x = y = z = s1 = s2 = t = np.zeros(N)
        p = np.ones(N)
        costheta = np.random.random(N)*2-1
        sintheta = 1-costheta*costheta
        sintheta[sintheta<0] = 0
        sintheta = np.sqrt(sintheta)
        phi = np.random.random(N)*(2*np.pi)
        cosphi = np.cos(phi)
        sinphi = np.sin(phi)
        v = self.v
        vz = v*costheta
        vx = v*sintheta * cosphi
        vy = v*sintheta * sinphi
        arr = np.array([x,y,z,vx,vy,vz, s1, s2, t, p]).T.copy()
        neutrons.from_npyarr(arr)
        return neutrons

def instrument(xml=None):
    instrument = mcvine.instrument()
    source = IsotropicSource('source', v=3000.)
    instrument.append(source, position=(0,0,0))

    if xml is not None:
        ds = mc.detectors.DetectorSystemFromXml('ds', xml, outfilename='events.dat')
        instrument.append(ds, position=(0,0,0))
    else:
        save = mc.monitors.NeutronToStorage('save', 'saved.mcv')
        instrument.append(save, position=(0,0,0))
    return instrument

# End of file
