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
fcc Ni scatterer constructed from an xml file
'''


import unittestX as unittest
import os



class TestCase(unittest.TestCase):

    interactive = False

    def _test(self):
        "fcc Ni scatterer constructed from an xml file"
        
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
            filename = 'IQE.dat'
            )
        from mcni.SimulationContext import SimulationContext
        component.simulation_context = SimulationContext()
        component.simulation_context.overwrite_datafiles = True
        component.simulation_context.outputdir = "out-fccNiphononkernelfromxml"
        component.simulation_context.iteration_no = 0
        
        scatterer = makeScatterer()
        
        import mcni
        N = 10000
        neutrons = mcni.neutron_buffer( N )
        for i in range(N):
            neutron = mcni.neutron(r=(0,0,0), v=(0,0,vi), time=0, prob=1)
            scatterer.scatter(neutron)
            neutrons[i] = neutron
            #print neutrons[i]
            continue
        
        component.process( neutrons )

        import histogram.hdf as hh
        outh5 = os.path.join(
            component.simulation_context.outputdir,
            'step0', 'IQE.h5')
        hist = hh.load(outh5)
        
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



def makeScatterer():
    import mccomponents.sample.phonon.xml
    from mccomponents.sample.kernelxml import parse_file
    scatterer = parse_file('fccNi-plate-scatterer-cubic-reciprocal-unitcell.xml')
    kernel = scatterer.kernel()

    from sampleassembly.predefined import shapes
    plate = shapes.plate(width=0.04, height=0.10, thickness=0.003)
    scatterer._shape = plate

    from sampleassembly import elements
    sample = elements.powdersample('fccNi', shape=plate)

    crystal = elements.crystal(unitcell=makeUnitcell())
    sample.phase = crystal

    kernel.scatterer_origin = sample
    
    from mccomponents.homogeneous_scatterer import scattererEngine
    return scattererEngine(scatterer)


# import matter package
def makeUnitcell():
    import diffpy.Structure as matter
    atoms = [matter.Atom('Ni')]
    # positions = [(0,0,0)]
    cellvectors = [ (3.57,0,0), (0,3.57,0), (0,0,3.57) ]
    lattice = matter.Lattice(base=cellvectors)
    return matter.Structure(lattice=lattice, atoms=atoms)



from mcstas2.components._proxies.monitors.IQE_monitor import get_histogram
import numpy as N


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    # TestCase.interactive = True
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
