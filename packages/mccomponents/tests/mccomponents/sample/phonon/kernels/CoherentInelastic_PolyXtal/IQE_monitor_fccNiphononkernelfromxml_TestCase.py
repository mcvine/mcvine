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
'''


import unittestX as unittest
import journal


componentname = 'IQE_monitor'
category = 'monitors'

class TestCase(unittest.TestCase):

    def test(self):
        "wrap IQE_monitor"
        
        from mcstas2 import componentfactory
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
        
        hist = _get_histogram(component)
        
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
    scatterer = parse_file('fccNi-plate-scatterer.xml')
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


def makeUnitcell():
    from crystal.UnitCell import create_unitcell
    from crystal.Atom import atom
    atoms = [atom('Ni')]
    positions = [(0,0,0)]
    cellvectors = [ (3.57,0,0), (0,3.57,0), (0,0,3.57) ]
    return create_unitcell(cellvectors, atoms, positions)



from mcstas2.pyre_support.monitor_exts.IQE_monitor import _get_histogram
import numpy as N


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    #journal.debug('phonon_coherent_inelastic_polyxtal_kernel').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
