# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

from . import mcvine, click

@mcvine.group(help='Commands to extract phonon dispersion curves from phonon data in IDF format')
def phonon():
    return

@phonon.command()
@click.argument("phonon")
@click.option("--start", default=(0.,0.,0.), help='start Q point')
@click.option("--end", default=(0.,0.,1.), help='stop Q point')
@click.option("--npts", default=100, help='number of points to sample')
@click.option("--cartesian", default=False, is_flag=True, help='indicate whether the Q points are in cartesian or hkl format')
@click.option("--output", default="", help="image file path to save the plot. empty means plotting interactively. Plotting requires matplotlib installed.")
@click.option("--branch", default=-1, help="0-based branch index. default value -1 means plot all branches")
def band(phonon, start, end, npts, cartesian, output, branch):
    "Plot band structure along one direction"
    # phonon is the path to a directory with IDF phonon data

    # read phonon data
    from mccomponents.sample.phonon import periodicdispersion_fromidf as pd
    import mcni, numpy as np
    disp = pd(phonon)
    # and construct the proxy to the c++ data object
    import mccomponents.homogeneous_scatterer as mh
    cdisp = mh.scattererEngine(disp)
    # create Q array
    Qs = np.array(start) + (np.array(end)-np.array(start)) * np.arange(0, 1, 1./npts)[:, np.newaxis]
    # Q will be cartesian
    if not cartesian:
        # read reciprocal basis vectors from Qgridinfo
        import os
        reci_basis = recibasis_fromQgridinfo(os.path.join(phonon, 'Qgridinfo'))
        Qs = np.dot(Qs, reci_basis)
    # compute energies
    nbr = disp.dispersion.nBranches
    Es = [cdisp.energy(br, mcni.vector3(*Q))
          for Q in Qs
          for br in range(nbr)]
    Es = np.array(Es)
    Es.shape = -1, nbr
    # output
    try:
        import pylab
    except ImportError:
        import warnings
        warnings.warn("Plotting needs matplotlib. Please install python matplotlib")
        return
    if branch == -1:
        for i in range(nbr):
            pylab.plot(Es[:, i])
    else:
        pylab.plot(Es[:, branch])
    if output:
        pylab.savefig(output)
    else:
        pylab.show()
    return


@phonon.command()
@click.argument("crystal")
@click.argument("phonon")
@click.option("--start", default=(0.,0.,0.), help='start Q point')
@click.option("--end", default=(0.,0.,1.), help='stop Q point')
@click.option("--npts", default=100, help='number of points to sample')
@click.option("--cartesian", default=False, is_flag=True, help='indicate whether the Q points are in cartesian or hkl format')
@click.option("--outhist", default="slice.h5", help="Output histogram file path")
@click.option("--Eaxis", default=(0., 100., 1.), help="Energy axis. (min, max, step)")
def slice(crystal, phonon, start, end, npts, cartesian, outhist, eaxis):
    "Compute slice of SQE data along a specific reciprocal space direction"
    # phonon is the path to a directory with IDF phonon data

    # read phonon data
    from mccomponents.sample.phonon import periodicdispersion_fromidf as pd
    import mcni, numpy as np
    disp = pd(phonon)
    # and construct a proxy to the c++ data object
    import mccomponents.homogeneous_scatterer as mh
    cdisp = mh.scattererEngine(disp)
    # create Q array
    start = np.array(start)
    end = np.array(end)
    step = (end-start)/npts
    Qs = start + step * np.arange(0, npts, 1.)[:, np.newaxis]
    # Qs: cartesian, hkls: miller indexes
    import os
    reci_basis = recibasis_fromQgridinfo(os.path.join(phonon, 'Qgridinfo'))
    inv_reci_basis = np.linalg.inv(reci_basis)
    if cartesian:
        hkls = np.dot(Qs, inv_reci_basis)
        # these vectors will be used later in method Qtox
        start = np.dot(start, inv_reci_basis)
        step = np.dot(step, inv_reci_basis)
        end = np.dot(end, inv_reci_basis)
    else:
        hkls = Qs
        Qs = np.dot(hkls, reci_basis)
    # gather energies and polarizations
    nQ = len(Qs)
    nbr = disp.dispersion.nBranches
    natoms = disp.dispersion.nAtoms
    # energies
    Es = [cdisp.energy(br, mcni.vector3(*Q)) 
          for Q in Qs 
          for br in range(nbr)
          ]
    Es = np.array(Es)
    Es.shape = nQ, nbr
    # polarizations
    pols = [
        np.array(cdisp.polarization(br, atom, mcni.vector3(*Q)))
        for Q in Qs
        for br in range(nbr)
        for atom in range(natoms)
        ]
    pols = np.array(pols)
    pols.shape = nQ, nbr, natoms, 3

    # get atom positions from crystal structure file
    from danse.ins.matter.Parsers import getParser
    parser = getParser(os.path.splitext(crystal)[-1][1:])
    structure = parser.parseFile(crystal)
    atom_positions = [atom.xyz for atom in structure]
    # create "events" for later histogramming process to construct slice
    events = computeEvents(hkls, Es, pols, atom_positions, reci_basis)
    # for x axis of the histogram (along Q)
    maxx = np.linalg.norm(end-start)
    xaxis = 0, maxx, maxx/npts
    # Eaxis = 0, np.max(Es) * 1.1, 1.
    Eaxis = eaxis
    # functor to convert hkl to "x" value
    def Qtox(hkl):
        x = np.linalg.norm(hkl-start, axis=-1)
        mask = x==x
        return x, mask
    # histogramming
    h = makeSlice(events, xaxis, Eaxis, Qtox)
    # output
    import histogram.hdf as hh
    hh.dump(h, outhist)
    return


def recibasis_fromQgridinfo(path):
    # read reciprocal basis vectors from Qgridinfo
    import os
    lines = open(path).readlines(3)
    d = {}
    for line in lines:
        exec(line, d)
        continue
    reci_basis = [d['b1'], d['b2'], d['b3']]
    return reci_basis


def computeEvents(Qs, omegas, pols, atom_positions, rec_lattice):
    """Given phonon data, generate events of (vector Q, E, and neutron scattering intensities)
    these events can be histogrammed into slice view of neutron scattering data.
    see below function makeSlice

    Qs, omegas, pols are numpy arrays
    They are generated from band.yaml.
    
    atom_positions: from POSCAR
    """
    import numpy as np
    nq, nbr = omegas.shape
    for iq, Q in enumerate(Qs):
        omega = omegas[iq]
        pol = pols[iq] # nbr, natom, ndim
        for br in range(nbr):
            E = omega[br]
            eps = pol[br] # natom, ndim
            
            Qdotr = np.dot(atom_positions, Q) * 2*np.pi 
            phase = np.exp(1j*Qdotr)

            # 
            Qdoteps = np.dot(eps, np.dot(Q, rec_lattice))
            
            # this phase factor is due to neutron wave
            # neutron wave reaches the atoms at different
            # position and time
            I = np.dot(phase, Qdoteps)
            
            I = np.absolute(I)**2 / E
            yield Q[0], Q[1], Q[2], E, I
            continue
        continue
    return


def makeSlice(events, xaxis, Eaxis, Qtox):
    """convert input events into a histogram (slice)
    
    Qtox:
    convert Q to x. also return a mask. since some Q points should be
    discarded
    """
    import numpy as np
    data = np.array(list(events))
    # convert Q to x
    Q = data[:, :3]
    x,mask = Qtox(Q)
    E = data[mask, 3]
    sample = np.vstack((x, E)).T
    #
    xbins = np.arange(*xaxis)
    Ebins = np.arange(*Eaxis)
    bins = xbins, Ebins
    weights = data[mask, -1]
    I, edges = np.histogramdd(sample, bins=bins, weights=weights)
    import histogram as H, histogram.hdf as hh
    axes = [
        H.axis('x', boundaries=edges[0]),
        H.axis('E', boundaries=edges[1]),
        ]
    return H.histogram('IxE', axes=axes, data = I)


# End of file 
