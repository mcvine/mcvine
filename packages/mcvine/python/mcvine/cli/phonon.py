# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

from . import mcvine, click

@mcvine.group()
def phonon():
    return

@phonon.command()
@click.argument("phonon")
@click.option("--start", default=(0.,0.,0.))
@click.option("--end", default=(0.,0.,1.))
@click.option("--npts", default=100)
@click.option("--cartesian", default=False, is_flag=True)
@click.option("--output", default="")
@click.option("--branch", default=-1)
def band(phonon, start, end, npts, cartesian, output, branch):
    "Plot band structure along one direction"
    # phonon is the path to a directory with IDF phonon data
    from mccomponents.sample.phonon import periodicdispersion_fromidf as pd
    import mcni, numpy as np
    disp = pd(phonon)
    import mccomponents.homogeneous_scatterer as mh
    cdisp = mh.scattererEngine(disp)
    Qs = np.array(start) + (np.array(end)-np.array(start)) * np.arange(0, 1, 1./npts)[:, np.newaxis]
    if not cartesian:
        # read reciprocal basis vectors from Qgridinfo
        import os
        reci_basis = recibasis_fromQgridinfo(os.path.join(phonon, 'Qgridinfo'))
        Qs = np.dot(Qs, reci_basis)
    nbr = disp.dispersion.nBranches
    Es = [cdisp.energy(br, mcni.vector3(*Q))
          for Q in Qs
          for br in range(nbr)]
    Es = np.array(Es)
    Es.shape = -1, nbr
    import pylab
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
@click.argument("phonon")
@click.option("--start", default=(0.,0.,0.))
@click.option("--end", default=(0.,0.,1.))
@click.option("--npts", default=100)
@click.option("--cartesian", default=False, is_flag=True)
@click.option("--output", default="")
def slice(phonon, start, end, npts, cartesian, output):
    "Plot slice of SQE data along a specific reciprocal space direction"
    # phonon is the path to a directory with IDF phonon data
    from mccomponents.sample.phonon import periodicdispersion_fromidf as pd
    import mcni, numpy as np
    disp = pd(phonon)
    import mccomponents.homogeneous_scatterer as mh
    cdisp = mh.scattererEngine(disp)
    start = np.array(start)
    end = np.array(end)
    step = (end-start)/npts
    Qs = start + step * np.arange(0, npts, 1.)[:, np.newaxis]
    import os
    reci_basis = recibasis_fromQgridinfo(os.path.join(phonon, 'Qgridinfo'))
    inv_reci_basis = np.linalg.inv(reci_basis)
    if cartesian:
        hkls = np.dot(Qs, inv_reci_basis)
        # start and step will be used later in method Qtox
        start = np.dot(start, inv_reci_basis)
        step = np.dot(step, inv_reci_basis)
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
    # !!! hack
    atom_positions = [[0,0,0]]
    events = computeEvents(hkls, Es, pols, atom_positions, reci_basis)

    xaxis = 0, 1, 2./npts
    Eaxis = 0, np.max(Es) * 1.1, 1.

    def Qtox(hkl):
        x = np.linalg.norm(hkl-start, axis=-1)/np.linalg.norm(step) / npts
        mask = x==x
        return x, mask
    
    h = makeSlice(events, xaxis, Eaxis, Qtox)
    import histogram.hdf as hh
    hh.dump(h, "IxE.h5")
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
    """
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
    """
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
