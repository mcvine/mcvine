#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


"""
This subpkg contains kernels for phonon scattering.

* incoherentelastic_kernel: elastic kernel with Debye Waller factor computed given phonon data.
* incoherentinelastic_kernel: incoherent single-phonon kernel
* multiphonon_kernel: multi-phonon kernel in incoherent approximation
* coherentinelastic_polyxtal_kernel: coherent phonon kernel for powder data
* coherentinelastic_singlextal_kernel: coherent phonon kernel for single crystal data.
  - In resolving a Q vector
    - the Q vector is first limited to 1BZ by periodicdispersion
    - then it is converted to hkl using the inverse of the reciprocal lattice vectors (obtained from the Qgridinfo file)

"""

import units
meV = units.energy.meV
angstrom = units.length.angstrom


def multiphonon_kernel(
    **kwds
    ):
    from MultiPhonon_Kernel import MultiPhonon_Kernel as f
    return f(**kwds)


def incoherentelastic_kernel(
    dw_core, **kwds
    ):
    from IncoherentElastic_Kernel import IncoherentElastic_Kernel as f
    return f( dw_core, **kwds )


def incoherentinelastic_kernel(
    dos, **kwds
    ):
    from IncoherentInelastic_Kernel import IncoherentInelastic_Kernel as f
    return f(dos, **kwds)


def coherentinelastic_polyxtal_kernel(
    dispersion, **kwds):
    from CoherentInelastic_PolyXtal_Kernel import CoherentInelastic_PolyXtal_Kernel as f
    return f( dispersion, **kwds)


def coherentinelastic_singlextal_kernel(
    dispersion
    ):
    from CoherentInelastic_SingleXtal_Kernel import CoherentInelastic_SingleXtal_Kernel as f
    return f( dispersion )


def linearlyinterpolateddispersion(
    nAtoms, dimension,
    Qaxes, eps_npyarr, E_npyarr,
    **kwds
    ):
    from LinearlyInterpolatedDispersionOnGrid \
         import LinearlyInterpolatedDispersionOnGrid
    return LinearlyInterpolatedDispersionOnGrid(
        nAtoms, dimension,
        Qaxes, eps_npyarr, E_npyarr,
        **kwds)


def periodicdispersion( dispersion, reciprocalcell ):
    from PeriodicDispersion import PeriodicDispersion
    return PeriodicDispersion( dispersion, reciprocalcell )


def dispersion_fromidf( datapath ):
    from mccomponents.sample.idf import readDispersion
    nAtoms, dimension, Qaxes, polarizations, energies, dos = readDispersion( datapath )
    
    dispersion = linearlyinterpolateddispersion(
        nAtoms, dimension,
        Qaxes, polarizations, energies, dos = dos )

    return dispersion


def periodicdispersion_fromidf( datapath ):
    dispersion = dispersion_fromidf( datapath )
    
    # XXX this is wasteful. should only need to read Qaxes, not everything
    from mccomponents.sample.idf import readDispersion
    nAtoms, dimension, Qaxes, polarizations, energies, dos = readDispersion( datapath )
    reciprocalcell = [ bi for bi,n in Qaxes ]
    
    return periodicdispersion(dispersion, reciprocalcell)


from .read_dos import *


import ComputationEngineRendererExtension

#make bindings available
def _import_bindings():
    import bindings
    return

_import_bindings()


# End of file 
