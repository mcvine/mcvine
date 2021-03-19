# -*- Python -*-

import numpy as np
import periodictable as pt
from .powder import Peak
# import tqdm

def iter_peaks(structure, T, max_index=5, type='powder'):
    "iterate over unique diffraction peaks"
    if type == 'powder':
        # when adding a peak, also add all its equivalent peaks to the "skip"
        # list, so that those peaks can be skipped over
        skip = set()
        hmin = kmin = lmin = 0
    elif type == 'singlecrystal':
        hmin = kmin = lmin = -max_index
    else:
        raise ValueError("type has to be powder or singlecrystal. got {}".format(type))
    hmax = kmax = lmax = max_index+1

    # for h in tqdm.tqdm(range(hmin, hmax)):
    for h in range(hmin, hmax):
        for k in range(kmin, kmax):
            for l in range(lmin, lmax):
                if h==0 and k==0 and l==0: continue
                hkl1 = h,k,l
                # print(hkl1)
                # for powder we don't want equivalent hkls
                if type == 'powder':
                    if hkl1 in skip: continue
                    eq_hkls = equivalent_hkls(hkl1, structure.sg)
                    eq_hkls = [tuple(map(int, _)) for _ in eq_hkls]
                    for _ in eq_hkls:
                        skip.add(_)
                    # print skip
                F1 = F(structure, hkl1, T)
                F_squared = np.abs(F1)**2 / 100 # from fm^2 to barn
                d1 = d(structure.lattice, hkl1)
                q1 = q(structure.lattice, hkl1)
                assert np.isclose(d1*q1, 2*np.pi)
                mult1 = multiplicity(hkl1, structure.sg)
                if np.abs(F1) > 1e-7:
                    yield Peak(hkl=hkl1, d=d1, q=q1, F=F1,
                               F_squared=F_squared, multiplicity=mult1)
    return


def q(lattice, hkl):
    "Returns q from (h, k, l) parameters"
    h,k,l   = hkl
    rb      = lattice.recbase
    q       = 2*np.pi*(h*rb[0] + k*rb[1] + l*rb[2])
    return np.sqrt(np.dot(q,q))

def F(structure, hkl, T):
    "structure factor. unit: fm"
    fs = [F_i(i, structure, hkl, T) 
          for i in range(len(structure))]
    return sum(fs)

def F_i(i, structure, hkl, T):
    from ..atomic_scattering import AtomicScattering
    atom = structure[i]
    element = atom.element
    element = ''.join([c for c in element if c.isalpha()])
    B = AtomicScattering(element).B(T)
    d1 = d(structure.lattice, hkl)
    position = atom.xyz
    o = atom.occupancy
    b = getattr(pt, element).neutron.b_c # unit: fm
    return o*b*np.exp(2*np.pi*1j*np.dot(hkl, position) - B/4/d1/d1)


def d(lattice, hkl):
    recbase = lattice.recbase # columns are rec base vectors
    recvec = np.dot(recbase, hkl)
    return 1./np.linalg.norm(recvec)


def multiplicity(hkl, sg):
    return len(equivalent_hkls(hkl, sg))


def equivalent_hkls(hkl, sg):
    vs = []
    for symop in sg.symop_list:
        v1 = np.dot(symop.R, hkl)
        added=False
        for v2 in vs:
            if np.isclose(v1, v2, atol=1e-7).all():
                added=True
                break
            continue
        if not added:
            vs.append(v1)
        continue
    return vs


# End of file
