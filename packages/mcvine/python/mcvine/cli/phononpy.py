#!/usr/bin/env python


import sys
import numpy as np
from phonopy.interface import vasp
from phonopy.units import VaspToTHz
from phonopy import Phonopy, file_IO

# some constants
THz2meV=4.1357

def compute(
    atom_chemical_symbols, qpoints, supercell_matrix, 
    freq2omega=THz2meV):
    
    # set up Si crystal lattice
    bulk = vasp.read_vasp("POSCAR", atom_chemical_symbols)
    
    # phonopy phonon instance
    phonon = Phonopy(bulk, supercell_matrix, distance=0.01, factor=VaspToTHz)
    # symmetry = phonon.get_symmetry()
    
    # report
    # print "Space group:", symmetry.get_international_table()
    # phonon.print_displacements()
    # supercells = phonon.get_supercells_with_displacements()

    # set force constants
    force_constants=file_IO.parse_FORCE_CONSTANTS('FORCE_CONSTANTS')
    phonon.set_force_constants(force_constants)

    # calc band structure
    # . compute
    phonon.set_qpoints_phonon(
        qpoints, is_eigenvectors=True,
        write_dynamical_matrices=False, factor=VaspToTHz)

    # output band structure
    # phonon.write_yaml_qpoints_phonon()

    # . get data
    freq, pols = phonon.get_qpoints_phonon()
    freq = freq * freq2omega
    pols = np.transpose(pols, (0, 2, 1))
    pols.shape = pols.shape[:-1] + (-1, 3)
    # pols: Q, branch, atom, xyz
    return qpoints, freq, pols


def test():
    N = 100
    Qz = np.arange(0, 1.+0.5/N, 1./N)
    Qx = np.zeros(Qz.size)
    Qy = np.zeros(Qz.size)
    Q = np.array([Qx, Qy, Qz])
    qpoints = Q.T
    supercell_matrix = [[3,0,0], [0,3,0], [0,0,3]]
    # !!! only need one symbol per specie
    # !!! follow vasp convention !!!
    atoms = ["Si"]
    qvecs, freq, pols = compute(atoms, qpoints, supercell_matrix)

    import pylab
    nbr = freq.shape[1]
    for i in range(nbr):
        pylab.plot(qvecs[:, 2], freq[:, i], 'k.')
        continue
    pylab.show()
    return


def test2():
    print "* Constructing Q array"
    delta = 0.01
    Qx = np.arange(0, 1.+delta/2, delta)
    Qy = np.arange(0, 1.+delta/2, delta)
    Qz = np.arange(0, 1.+delta/2, delta)
    Qs = []
    for qx in Qx:
        for qy in Qy:
            for qz in Qz:
                Qs.append([qx,qy,qz])
                continue
    Qs =  np.array(Qs)
    
    supercell_matrix = [[3,0,0], [0,3,0], [0,0,3]]
    # !!! only need one symbol per specie
    # !!! follow vasp convention !!!
    atoms = ["Si"]
    print "* Calling phonopy to compute eigen values and eigen vectors"
    qvecs, freq, pols = compute(atoms, Qs, supercell_matrix, freq2omega=1)
    
    print "* Writing out freqencies"
    from mccomponents.sample.idf import Omega2, Polarizations
    omega2 = freq**2 * 1e24 * (2*np.pi)**2
    Omega2.write(omega2)

    # phase factor for pols
    print "* Fixing and writing out polarizations"
    nq, nbr, natoms, three = pols.shape
    assert three is 3
    atoms = vasp.read_vasp("POSCAR", ['Si'])
    positions = atoms.get_scaled_positions()
    for iatom in range(natoms):
        qdotr = np.dot(Qs, positions[iatom]) * 2 * np.pi
        phase = np.exp(1j * qdotr)
        pols[:, :, iatom, :] *= phase[:, np.newaxis, np.newaxis]
        continue
    Polarizations.write(pols)
    return

if __name__ == '__main__': test2()
