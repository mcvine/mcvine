# -*- Python -*-

import numpy as np
from . import matter
import periodictable as ptbl
from .vogel import phi1

"Implementation follows section 3.2.1 of Vogel's thesis"

class AtomicScattering:

    """This class gather methods related to calculation of scattering
    property of an element. So the name "AtomicScattering" is not 
    really accurate.
    """

    def __init__(self, element, occupancy=1.):
        self.element = element
        self.atom = matter.Atom(element)
        import periodictable as pt
        self.ns = getattr(pt, keepletters(element)).neutron # neutron scattering lengths, cross sections etc
        self.occupancy = occupancy
        return

    def sigma_abs(self):
        "absorption cross section"
        return self.ns.absorption

    def b(self):
        "bound scattering length"
        return self.ns.b_c

    def theta(self, T):
        element = self.element
        TD = getDebyeTemp(element)
        return 1.*T/TD

    def B(self, T):
        element = self.element
        atom = self.atom
        mass = getattr(ptbl, keepletters(atom.element)).mass
        T_D = getDebyeTemp(element)
        theta1 = self.theta(T)
        rt = 3*h*h*phi1(theta1)/(mass*amu*kB*T_D)
        # convert to AA
        return rt/AA/AA

def getDebyeTemp(element):
    default = 1000.
    from .DebyeTemp import getT
    T = getT(element, None)
    if T is None:
        import warnings
        warnings.warn("Debye temperature for {} is set to {}".format(element, default))
        T = default
    return T

def keepletters(s):
    return ''.join(x for x in s if x.isalpha())

h = 6.62607004e-34
kB = 1.38064852e-23
AA = 1e-10
amu = 1.660539040e-27

def test():
    assert np.isclose(AtomicScattering('Ni').B(300), 0.307, rtol=1e-2)

if __name__ == '__main__': test()

# End of file
