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

def create_peaks_py(path, structure, T, max_index=5):
    from . import calcpeaks
    pks = list(calcpeaks.iter_peaks(structure, T, max_index))
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
