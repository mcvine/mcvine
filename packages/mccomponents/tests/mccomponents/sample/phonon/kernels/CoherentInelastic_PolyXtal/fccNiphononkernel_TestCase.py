#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2009 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''
This is a test of the phonon coherent inelastic scattering kernel.
This test constructs dispersion from a idf data directory, and
the kernel engine is constructed from calling the engine renderer
on the kernel python representation.
'''


skip = True
need_user_interaction = True


import unittestX as unittest
import journal



class TestCase(unittest.TestCase):
    
    interactive = False

    def test(self):
        "fccNi kernel constructed by hand"
        
        from mcstas2 import componentfactory
        category = 'monitors'
        componentname = 'IQE_monitor'
        factory = componentfactory( category, componentname )

        Qmin=0; Qmax=13.; nQ=130
        Emin=-50; Emax=50.; nE=100
        
        component = factory(
            'component',
            Ei=Ei,
            Qmin=Qmin, Qmax=Qmax, nQ=nQ,
            Emin=Emin, Emax=Emax, nE=nE,
            max_angle_out_of_plane=30, min_angle_out_of_plane=-30,
            max_angle_in_plane=120, min_angle_in_plane=-30,
            )

        kernel = makeKernel()
        
        import mcni
        # N = 500000 # needs about 20 minutes on a Intel Core2 Duo 2.53GHz virtual machine, ubuntu 10.04LTS on a 2.53GHz Intel Core 2 Duo Macbook
        N = 10000
        neutrons = mcni.neutron_buffer( N )
        for i in range(N):
            neutron = mcni.neutron(r=(0,0,0), v=(0,0,vi), time=0, prob=1)
            kernel.scatter(neutron)
            neutrons[i] = neutron
            #print neutrons[i]
            continue
        
        component.process( neutrons )
        hist = get_histogram(component)
        
        if self.interactive:
            from histogram.plotter import defaultPlotter
            defaultPlotter.plot(hist)
        return

    pass  # end of TestCase



mass = 50
temperature = 300
Ei = 70
from mcni.utils import conversion as C
vi = C.e2v(Ei)
dispersion_dir = 'phonon-dispersion-fccNi-cubic-reciprocal-unitcell'


def makeKernel():
    max_omega = 50
    max_Q = 13
    nMCsteps_to_calc_RARV = 1000
    return b.phonon_coherentinelastic_polyxtal_kernel(
        makeDispersion(), makeDW(),
        makeUnitcell(),
        temperature=temperature, Ei=Ei, max_omega=max_omega, max_Q=max_Q,
        nMCsteps_to_calc_RARV=nMCsteps_to_calc_RARV)


def makeUnitcell():
    from diffpy import Structure
    atoms = [Structure.Atom('Ni')]
    # positions = [(0,0,0)]
    cellvectors = [ (3.57,0,0), (0,3.57,0), (0,0,3.57) ]
    lattice = Structure.Lattice(base=cellvectors)
    return Structure.Structure(lattice=lattice, atoms=atoms)


def mkDOS():
    e0 = 0
    de = 0.5
    n = 100
    Z = N.arange(0,1,0.01)
    return b.linearlyinterpolateddos(e0, de, n, Z)


def makeDW():
    nsampling = 100
    return b.dwfromDOS(mkDOS(), mass, temperature, nsampling)
    

def makeDispersion():
    from mccomponents.sample.phonon import periodicdispersion_fromidf
    disp = periodicdispersion_fromidf(dispersion_dir)
    from mccomponents.homogeneous_scatterer import kernelEngine, scattererEngine
    disp = scattererEngine(disp)
    return disp


import mccomponents.sample.phonon.bindings as bindings
b = bindings.get('BoostPython')

from mcstas2.components._proxies.monitors.IQE_monitor import get_histogram
import numpy as N


def pysuite():
    TestCase.interactive = True
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    #journal.debug('phonon_coherent_inelastic_polyxtal_kernel').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
