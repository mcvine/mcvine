#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#



from .base import Component as base

class Component(base):

    def _get_histogram(self):
        norm = self._get_normalization()
        h = get_histogram(self._cpp_instance)
        return h/norm

    
    def _get_normalization(self):
        if hasattr(self, '_norm'):
            norm = self._norm
        else:
            norm = self._norm = self._get_normalization_p()
        return norm


    def _get_normalization_p(self):
        context = self.simulation_context
        # the master node need to compute the norm
        if not context.mpiRank:
            norm = getNormalization(self._cpp_instance, factory=self._cpp_instance_factory)
        # if there are no other nodes, we are fine
        if not context.mpiSize:
            return norm
        # otherwise, need to send norm to all nodes
        channel = self.mpi.getUniqueChannel()
        if context.mpiRank == 0:
            for node in range(1, context.mpiSize):
                self.mpi.send(norm, node, channel)
                continue
        else:
            norm = self.mpi.receive(0, channel)
        return norm


def get_histogram( monitor ):
    from mcstas2.utils.carray import bpptr2npyarr
    core = monitor.core()

    nQ = core.nQ; nE =core.nE
    n = nQ * nE
    shape = nQ, nE

    Iarr = bpptr2npyarr( core.getIQE_p( ), 'double', n ).copy()
    E2arr = bpptr2npyarr( core.getIQE_p2( ), 'double', n ).copy()
    Iarr.shape = E2arr.shape = shape

    from histogram import histogram, axis, arange
    dE = (core.Emax-core.Emin)/nE
    Eaxis = axis( 'energy', arange( core.Emin, core.Emax, dE ), unit = 'meV' )

    dQ = (core.Qmax-core.Qmin)/nQ
    Qaxis = axis( 'Q', arange( core.Qmin, core.Qmax, dQ ), unit = 'angstrom**-1' )

    h = histogram( 'I(Q,E)', [Qaxis,Eaxis], data = Iarr, errors = E2arr )
    return h


def getNormalization(monitor, N=None, epsilon=1e-7, factory=None):
    # randomly shoot neutrons to monitor in 4pi solid angle
    print("* start computing normalizer...")
    core = monitor.core()
    if N is None:
        N = core.nQ * core.nE * 10000
    
    import mcni, random, mcni.utils.conversion as conversion, math, os
    import numpy as np

    # incident velocity
    vi = conversion.e2v(core.Ei)
    
    # 1. create neutrons
    def make_neutrons(N):
        neutrons = mcni.neutron_buffer(N)
        #
        # randomly select E, the energy transfer
        E = core.Emin + np.random.random(N) * (core.Emax-core.Emin)
        # the final energy
        Ef = core.Ei - E
        # the final velocity
        vf = conversion.e2v(Ef)
        # choose cos(theta) between -1 and 1
        cos_t = np.random.random(N) * 2 - 1
        # theta
        theta = np.arccos(cos_t)
        # sin(theta)
        sin_t = np.sin(theta)
        # phi: 0 - 2pi
        phi = np.random.random(N) * 2 * np.pi
        # compute final velocity vector
        vx,vy,vz = vf*sin_t*np.cos(phi), vf*sin_t*np.sin(phi), vf*cos_t
        # neutron position, spin, tof are set to zero
        x = y = z = sx = sy = t = np.zeros(N, dtype="float64")
        # probability
        prob = np.ones(N, dtype="float64") * (vf/vi)
        # XXX: this assumes a specific data layout of neutron struct
        n_arr = np.array([x,y,z,vx,vy,vz, sx,sy, t, prob]).T.copy()
        neutrons.from_npyarr(n_arr)
        return neutrons
    
    # 2. create a copy of the original monitor
    props = [
        'Ei',
        'Emin', 'Emax', 'nE',
        'Qmin', 'Qmax', 'nQ',
        'max_angle_out_of_plane', 'min_angle_out_of_plane',
        'max_angle_in_plane', 'min_angle_in_plane',
        ]
    kwds = {}
    for p in props: kwds[p] = getattr(core, p)
    import tempfile
    tmpdir = tempfile.mkdtemp()
    outfilename = os.path.join(tmpdir, 'mon.dat')
    kwds['filename'] = outfilename
    cppmonitorcopy = factory('monitor', **kwds)
    
    # 3. send neutrons to monitor copy
    N1 = 0; dN = int(1e6)
    print("  - total neutrons needed :", N)
    while N1 < N:
        n = min(N-N1, dN)
        neutrons = make_neutrons(n)
        cppmonitorcopy.process(neutrons)
        N1 += n
        print("  - processed %s" % N1)
        continue
    h = get_histogram(cppmonitorcopy)
    # for debug
    # import histogram.hdf as hh
    # hh.dump(h, 'tmp.h5', '/', 'c')
    h.I[h.I<epsilon] = 1
    #
    print("  - done computing normalizer")
    return h


def test1():
    from mcstas2 import componentfactory
    cf = componentfactory(type='IQE_monitor', category='monitors')
    monitor = cf('monitor')
    getNormalization(monitor._cpp_instance, N=1000000)
    return


def main():
    test1()
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"


# End of file 
