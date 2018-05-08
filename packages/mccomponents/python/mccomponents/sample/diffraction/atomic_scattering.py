# -*- Python -*-

import numpy as np
from danse.ins import matter
from .vogel import phi1


class AtomicScattering:
    
    """This class gather methods related to calculation of scattering
    property of an element. So the name "AtomicScattering" is not 
    really accurate.
    """

    def __init__(self, element, occupancy=1.):
        self.element = element
        self.atom = matter.Atom(element)
        import periodictable as pt
        self.ns = getattr(pt, element).neutron # neutron scattering lengths, cross sections etc
        self.occupancy = occupancy
        return


    def b(self):
        "bound scattering length"
        return self.ns.b_c


    def sigma_inc(self):
        "incoherent scattering cross section"
        return self.ns.incoherent


    def sigma_abs(self):
        "absorption cross section"
        return self.ns.absorption


    def S_el_inc(self, lambda1, T):
        B = self.B(T)
        l2 = lambda1**2
        exponent = 2*B/l2
        return 1./exponent*(1-np.exp(-exponent))


    def S_total_inc(self, lambda1, T):
        atom = self.atom
        mass = atom.mass
        m_r = mass/1.
        theta1 = self.theta(T)
        from . import vogel
        phi3 = vogel.phi3(theta1)
        phi1 = vogel.phi1(theta1)
        B = self.B(T)
        return (m_r/(m_r+1))**2 * (1+4.5/m_r/m_r*phi3*phi1*lambda1**2/B)


    def S_inel_inc(self, lambda1, T):
        return self.S_total_inc(lambda1, T) - self.S_el_inc(lambda1, T)


    def theta(self, T):
        element = self.element
        from DebyeTemp import getT
        return 1.*T/getT(element)


    def B(self, T):
        element = self.element
        atom = self.atom
        mass = atom.mass
        from DebyeTemp import getT
        T_D = getT(element)
        theta1 = self.theta(T)
        rt = 3*h*h*phi1(theta1)/(mass*amu*kB*T_D)
        # convert to AA
        return rt/AA/AA


h = 6.62607004e-34
kB = 1.38064852e-23
AA = 1e-10
amu = 1.660539040e-27

def test():
    assert np.isclose(AtomicScattering('Ni').B(300), 0.307, rtol=1e-2)


if __name__ == '__main__': test()

# End of file
