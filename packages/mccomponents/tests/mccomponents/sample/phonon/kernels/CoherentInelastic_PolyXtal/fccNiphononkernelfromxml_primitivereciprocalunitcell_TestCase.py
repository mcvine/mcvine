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


skip = True
need_user_interaction = True

'''
'''


import unittestX as unittest


class TestCase(unittest.TestCase):

    interactive = False

    def test(self):
        "wrap IQE_monitor"
        
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

        from mcni.SimulationContext import SimulationContext
        component.simulation_context = SimulationContext(outputdir="out-fccNiphononkernelfromxml_primitivereciprocalunitcell_TestCase")
        component.process( neutrons )
                
        if self.interactive:
            from histogram.plotter import defaultPlotter
            defaultPlotter.plot(os.path.join(component.simulation_context.outputdir, 'IQE.h5'))
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
    scatterer = parse_file('fccNi-plate-scatterer-primitive-reciprocal-unitcell.xml')
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
    from diffpy import Structure as matter
    atoms = [matter.Atom('Ni')]
    # positions = [(0,0,0)]
    cellvectors = [ (3.57,0,0), (0,3.57,0), (0,0,3.57) ]
    lattice = matter.Lattice(base=cellvectors)
    return matter.Structure(lattice=lattice, atoms=atoms)



if __name__ == "__main__": unittest.main()

    
# End of file 
