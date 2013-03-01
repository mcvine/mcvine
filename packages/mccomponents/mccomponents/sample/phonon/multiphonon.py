#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2005-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
compute S(Q,E) from phonon DOS

We follow the formulas in section
"Calculation of Multiphonon Scattering"
of the book 
"Experimental Inelastic Neutron Scattering".

Some of the implementation here were taken from
Max Kresch's original multiphonon code.
"""


def sqe(E, g, Qmax=None, Qmin=0, dQ=None, T=300, M=50, N=5):
    """compute sum of multiphonon SQE from dos
    S = \sum_{i=2,N} S_i(Q,E)
    
    Note: single phonon scattering is not included. only 2-phonons and up
    
    E,g: input DOS data
    energy axis is inferred from input DOS data
    Q axis is defined by Qmax, Qmin, and dQ
    T: temperature (Kelvin)
    M: atomic mass 
    N: maximum number of order for multi-phonon scattering
    """
    dos_sample = len(E)
    e0 = E[0]
    de = E[1] - E[0]
    emax = E[-1]
    # expand E
    E = np.arange(e0, e0+de*3*dos_sample, de)
    g = np.concatenate((g, np.zeros(len(E)-len(g))))
    # normalize
    int_g = np.sum(g) * de
    g/=int_g
    # Q axis
    if Qmax is None:
        from mcni.utils import conversion
        Qmax = conversion.e2k(emax) * 3
    if dQ is None:
        dQ = (Qmax-Qmin)/200
    Q = np.arange(Qmin, Qmax, dQ)
    
    # beta
    kelvin2mev = 0.0862
    beta = 1./(T*kelvin2mev)
    
    # compute S
    from mccomponents.sample.phonon.multiphonon import computeSQESet
    Q, E, S_set= computeSQESet(N, Q, dQ, E, de, M, g, beta)
    
    # sum over 2..N
    S = S_set[1:].sum(axis=0)
    return Q, E, S


def computeSQESet(N, Q,dQ, E,dE, M, g, beta):
    """compute the set of S(Q,E) for n in [1,N]
    Q, dQ: Q axis
    E, dE: E axis
    M: mass
    g: phonon DOS for the given E
    beta: 1/(kBT)
    """
    
    E2, AnE_set = computeAnESet(N, E,g, beta, dE)
    
    DW2 = DWExp(Q, M, E,g, beta, dE)
    SnQ_set = computeSnQSet(N, DW2)
    
    sqe = []
    for S, A in zip(SnQ_set, AnE_set):
        sqe.append(np.outer(S, A))
        continue
    sqe = np.array(sqe)
    return Q, E2, sqe


def computeSnQSet(N, DW2):
    """ compute the set of Sn(Q) for n in [1,N]
    """
    SNQ = []
    for i in range(1,N+1):
        SNQ.append(computeSNQ(DW2,i))
    return np.array(SNQ)


def computeSNQ(DW2,N):
    """ Takes the exponent for the Debye Waller factor `DW2` = 2W, and an
    integer N indicating a term in the phonon expansion and returns the 
    intensity of the N-phonon incoherent scattering S_N(Q)
    """
    return DW2**N * np.exp(-DW2) / float(math.factorial(N))


def computeAnESet(N, E,g, beta, dE):
    """compute the set of An(E) for n in [1,N]
    """
    ANE = []
    E, A1E = computeA1E(E,g, beta, dE)
    ANE.append(A1E)
    
    for i in range(2,N+1): 
        ANE.append(AnE_from_n_1(ANE[0], ANE[-1], dE))
        continue
    return E, np.array(ANE)


def AnE_from_n_1(A1E, Anm1E, dE):
    """compute A_n(E) from A_{n-1}(E)

    A_n(E) = A1 (convolve) A_{n-1}
    """
    Y = np.zeros( 4*len(Anm1E),'d' )
    Y[len(A1E):2*len(A1E)] = Anm1E
    y = np.zeros( 3*len(A1E),'d' )
    y = np.concatenate((y, A1E), axis=0)
    y = y[::-1]
    M = convMatrix(y)
    res = np.inner(M,Y)
    res *= dE
    start = len(A1E)/2+1
    t = res[start:start + len(A1E)]
    # XXX: normalize?
    # t/= t.sum()
    return t


def convMatrix(y):
    """ Returns matrix M, whose rows are filled with shifted copies of vector y"""
    M = np.zeros( ( len(y),len(y) ) , 'd' )
    for i in range(len(y)):
        M[i,i:] = y[:len(y)-i]
    return M


def computeA1E(E,g, beta, dE):
    """compute A_1(E)
    
    A_1(E) = g(E)/(E*gamma_0) / (exp(E/kBT) - 1)

    E,g: numpy arrays of energies and density of states
         it must be normalized

    output: npy array of A1E 
    **note**: if the input energy array for DOS has N elements
              the output has 2N-1 elements, since the input 
              energies are in [0, Emax], while the output energies 
              are in [-Emax, Emax]
    """
    zero_ind = len(E) - 1
    g0 = gamma0(E,g, beta, dE)
    E, g = reflected(E,g)
    # t = 1./(np.exp(E*beta) - 1) # XXX
    t = 1./(1-np.exp(-E*beta)) # XXX
    t = g/(E*g0)*t
    z = zero_ind
    # remove NaN
    t[z] = 2.0*( t[z+1] + ( t[z+1] - t[z+2] ) ) # XXX: why 2.0* ?
    # XXX: normalize?
    # t /= t.sum()
    return E, t


def reflected(x,y):
    """compute reflected function
    
    the input x array must starts with 0
    the result is xr, yr tuple

    The reflected function has the property
    y(-x) = y(x)
    """
    def reflect(a, multiplier):
        t = (multiplier*a).tolist()
        t.reverse()
        return np.concatenate( (t, a[1:]), 0 )
    return reflect(x, -1), reflect(y, 1)

    
def coth(x):
    return np.cosh(x)/np.sinh(x)

def gamma0(E, g, beta, dE):
    """Compute gamma0
    gamma0 = \int coth(E/2kBT) g(E)/E dE

    E,g: numpy arrays of energies and density of states
         it must be normalized
    beta: 1/kBT
    dE:  delta E in E array
    """
    dos_integrated = np.sum(g)*dE
    assert abs(dos_integrated - 1) < 1e-3
    f = coth(beta * E/2.) * g/E * dE
    f[0] = f[1] + (f[1] - f[2] ) # Define unidentified value, i.e. initial value.
    return np.sum(f)


def DWExp(Q, M, E,g, beta, dE):
    """compute 2W, the exponent of the Debye Waller factor. 
    """
    g0 =  gamma0(E,g, beta, dE)
    Er = recoilE(Q, M)
    return Er*g0


def recoilE(Q, M):
    """compute recoil energy E_r(Q)
    """
    return J2meV * ( h_b*Q/A2m )**2.0 / 2.0 / (M*amu)


""" 
Some physical constants in mks units, and some conversions to units 
convenient for neutron scattering.

A2m   = multiply by this to take Angstroms to meters
J2meV = multiply by this to convert Joules to meV 
amu   = mass of `atomic mass unit`
h     = Planck's constant
h_b   = Planck's constant / 2 pi
k_b   = Boltzmann's constant 
m_n   = Neutron mass
"""
A2m   =   1.0e-10         # multiplication by takes Angstroms to meters
J2meV =   6.2415097e+21   # multiplication by takes Joules to meV
amu   =   1.66053873e-27  # kg
h     =   6.6260688e-34   # kg m^2 / s
h_b   =   1.0545716e-34   # kg m^2 / s
k_b   =   1.3806503e-23   # kg m^2 / K s^2
m_n   =   1.6749272e-27   # kg


import numpy as np, math


# version
__id__ = "$Id$"

# End of file 
