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


from . import units
meV = units.energy.meV
angstrom = units.length.angstrom


def singlecrystaldiffractionkernel(
        basis_vectors, hkllist, mosaic, Dd_over_d, abs_xs
    ):
    from .SingleCrystalDiffractionKernel import SingleCrystalDiffractionKernel as f
    return f(basis_vectors, hkllist, mosaic, Dd_over_d, abs_xs)

def simplepowderdiffractionkernel(
    Dd_over_d, DebyeWaller_factor, peaks, **kwds
    ):
    from .SimplePowderDiffractionKernel import SimplePowderDiffractionKernel as f
    return f(Dd_over_d, DebyeWaller_factor, peaks, **kwds)

def create_lau(path, structure, T, max_index=5, min_dspacing=None):
    from . import calcpeaks
    pks = list(calcpeaks.iter_peaks(
        structure, T, max_index, min_dspacing=min_dspacing, type='singlecrystal'))
    content = []
    lattice = structure.lattice
    header = '''# CELL {a} {b} {c} {alpha} {beta} {gamma}
# column_j  4 multiplicity 'j'
# column_d  5 d-spacing 'd' in [Angs]
# column_F2 6 norm of scattering factor |F|^2 in [fm^2]
# column_h  1
# column_k  2
# column_l  3
# h   k   l Mult. d-space  F-squared
'''.format(a=lattice.a, b=lattice.b, c=lattice.c,
           alpha=lattice.alpha, beta=lattice.beta, gamma=lattice.gamma)
    for pk in pks:
        h,k,l = pk.hkl
        line = '{h} {k} {l} {mul} {d} {F2}'.format(
            h=h,k=k,l=l, mul=pk.multiplicity, d=pk.d,
            F2=pk.F_squared*100, # pk.F_squared is in barns. convert to fm^2
        )
        content.append(line)
    content = [header] + content
    with open(path, 'wt') as stream:
        stream.write('\n'.join(content))
    return

def create_peaks_py(path, structure, T, max_index=5, min_dspacing=None):
    from . import calcpeaks
    pks = list(calcpeaks.iter_peaks(structure, T, max_index, min_dspacing=min_dspacing))
    lines_for_peaks = [str(pk) for pk in pks]
    qs = [pk.q for pk in pks]
    lines_for_peaks = [l for (q, l) in sorted(zip(qs, lines_for_peaks))]
    lines_for_peaks = ',\n'.join('    '+l for l in lines_for_peaks)
    lattice = structure.lattice
    unitcell_volume = lattice.volume
    abs_xs = _abs_xs(structure)
    content = '''from mccomponents.sample.diffraction.SimplePowderDiffractionKernel import Peak

peaks = [
%(lines_for_peaks)s
    ]

# unit: \AA
unitcell_volume = %(unitcell_volume)s

# unit: barns
class cross_sections:
    coh = 0
    inc = 0
    abs = %(abs_xs)s
''' % locals()
    open(path, 'wt').write(content)
    return
    

from . import ComputationEngineRendererExtension

#make bindings available
def _import_bindings():
    from . import bindings
    return

_import_bindings()


def _abs_xs(structure):
    import numpy as np
    occs = np.array([atom.occupancy for atom in structure])
    from ..atomic_scattering import AtomicScattering as AS
    sctts = [AS(atom.element, occupancy=atom.occupancy) for atom in structure]
    abs_xss = np.array([sc.sigma_abs() for sc in sctts])
    return np.sum(occs*abs_xss)
    


# version
__id__ = "$Id$"

# End of file 
