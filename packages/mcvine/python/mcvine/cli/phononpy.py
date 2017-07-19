#!/usr/bin/env python


from . import mcvine, click

@mcvine.group(help='Commands to run phonopy to compute phonon data in IDF format')
def phononpy():
    return


@phononpy.command()
@click.argument("")
@click.option("--force-constants", default='FORCE_CONSTANTS', help='path of the FORCE_CONSTANTS file')
@click.option("--poscar", default='POSCAR', help='path of the POSCAR file')
@click.option("--species", default="Si", help='comma-separated list of atomic species')
@click.option("--supercell-matrix", default=[[5,0,0], [0,5,0], [0,0,5]], help='supercell matrix')
@click.option("--qgrid-dims", default=[51, 51, 51], help='Q grid dimensions')
def griddisp(force_constants, poscar, species, supercell, qgrid_dims):
    species = species.split(',')
    print "* Constructing Q array"
    qgrid_dims = np.array(qgrid_dims, dtype=float)
    delta = 1./(qgrid_dims-1)
    Qx = np.arange(0, 1.+delta[0]/2, delta[0])
    Qy = np.arange(0, 1.+delta[1]/2, delta[1])
    Qz = np.arange(0, 1.+delta[2]/2, delta[2])
    Qs = []
    for qx in Qx:
        for qy in Qy:
            for qz in Qz:
                Qs.append([qx,qy,qz])
                continue
    Qs =  np.array(Qs)
    
    # !!! only need one symbol per specie
    # !!! follow vasp convention !!!
    force_constants=file_IO.parse_FORCE_CONSTANTS(force_constants)
    
    print "* Calling phonopy to compute eigen values and eigen vectors"
    qvecs, freq, pols = compute(species, Qs, supercell_matrix, poscar, force_constants, freq2omega=1)
    
    print "* Writing out freqencies"
    from mccomponents.sample.idf import Omega2, Polarizations
    omega2 = freq**2 * 1e24 * (2*np.pi)**2
    Omega2.write(omega2)

    # phase factor for pols
    print "* Fixing and writing out polarizations"
    nq, nbr, natoms, three = pols.shape
    assert three is 3
    atoms = vasp.read_vasp(poscar, species)
    positions = atoms.get_scaled_positions()
    for iatom in range(natoms):
        qdotr = np.dot(Qs, positions[iatom]) * 2 * np.pi
        phase = np.exp(1j * qdotr)
        pols[:, :, iatom, :] *= phase[:, np.newaxis, np.newaxis]
        continue
    Polarizations.write(pols)
    return


import sys
import numpy as np

# some constants
THz2meV=4.1357

def compute(
        atom_chemical_symbols, qpoints, supercell_matrix,
        poscar, force_constants,
        freq2omega=THz2meV):
    
    from phonopy.interface import vasp
    from phonopy.units import VaspToTHz
    from phonopy import Phonopy, file_IO

    # set up Si crystal lattice
    bulk = vasp.read_vasp(poscar, atom_chemical_symbols)
    
    # phonopy phonon instance
    phonon = Phonopy(bulk, supercell_matrix, factor=VaspToTHz)
    phonon.generate_displacements(distance=0.01)
    # symmetry = phonon.get_symmetry()
    
    # report
    # print "Space group:", symmetry.get_international_table()
    # phonon.print_displacements()
    # supercells = phonon.get_supercells_with_displacements()

    # set force constants
    phonon.set_force_constants(force_constants)

    # calc band structure
    # . compute
    phonon.set_qpoints_phonon(
        qpoints, is_eigenvectors=True,
        write_dynamical_matrices=False) #, factor=VaspToTHz)

    # output band structure
    # phonon.write_yaml_qpoints_phonon()

    # . get data
    freq, pols = phonon.get_qpoints_phonon()
    freq = freq * freq2omega
    pols = np.transpose(pols, (0, 2, 1))
    pols.shape = pols.shape[:-1] + (-1, 3)
    # pols: Q, branch, atom, xyz
    return qpoints, freq, pols

