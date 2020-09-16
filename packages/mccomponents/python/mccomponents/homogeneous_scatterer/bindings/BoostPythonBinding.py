#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import mccomposite.bindings
mccomposite.bindings.get('BoostPython')
import mccomponents.mccomponentsbp as binding


from .AbstractBinding import AbstractBinding as Interface
from mccomposite.bindings.BoostPythonBinding import BoostPythonBinding as base


class BoostPythonBinding(base):
# class BoostPythonBinding:

    '''factory class of boost python computing engine of scatterers
    '''

    def srandom(self, seed):
        return binding.srandom( seed )
    

    def compositekernel(self, kernels, weights, rotmats, average):
        return binding.CompositeScatteringKernel(
            kernels, weights, rotmats, average )


    def kernelcontainer(self, size = 0):
        return binding.pointer_vector_Kernel( size )


    def homogeneousscatterer(
            self, shape, kernel, weights, 
            max_multiplescattering_loops, min_neutron_probability, packing_factor,
            mu_calculator
        ):
        cweights = binding.MCWeights_AbsorptionScatteringTransmission( *weights )
        if mu_calculator is None:
            engine = binding.HomogeneousNeutronScatterer(shape, kernel, cweights )
        else:
            engine = binding.HomogeneousNeutronScatterer(shape, kernel, mu_calculator, cweights )
        engine.max_multiplescattering_loops = max_multiplescattering_loops
        engine.min_neutron_probability = min_neutron_probability
        engine.packing_factor = packing_factor
        engine.mu_calculator = mu_calculator
        return engine


    def inversevelocityabsorption(self, mu_at_2200):
        return binding.InverseVelocityAbsorption(mu_at_2200)
    
    
    def interpolateabsorptionfromcurve(self, energies, mus):
        cenergies = self.list_to_vector_double(energies)
        cmus = self.list_to_vector_double(mus)
        return binding.InterpolateAbsorptionFromCurve(cenergies, cmus)
    
    
    def vector_double(self, size):
        return binding.vector_double(size)

    def vector_rotmat(self):
        return binding.vector_rotmat(0)

    def list_to_vector_double(self, l):
        vec = self.vector_double(len(l))
        for i, v in enumerate(l):
            vec[i] = l[i]
            continue
        return vec    

    pass # end of BoostPythonBinding


def register( methodname, method, override = False ):
    '''register a new handling method'''
    if hasattr(BoostPythonBinding, methodname):
        if not override:
            raise ValueError("Cannot register handler %s. "\
                  "It was already registered." % (
                methodname ))
        pass
    
    setattr( BoostPythonBinding, methodname, method )

    return

_original = BoostPythonBinding
_klasses = [_original]
def extend( klass ):
    "extend binding class with the new class"
    if klass in _klasses: return
    _klasses.insert(0, klass)
    import sys
    if sys.version_info < (3,0):
        BPB = _klasses[-1]
        for kls in _klasses[-2::-1]:
            K = BPB
            class BPB(kls, K): pass
            continue
    else:
        from ._py3 import make_subclass
        BPB = make_subclass(_klasses)
    BPB.__name__ = 'BoostPythonBinding'
    global BoostPythonBinding
    BoostPythonBinding = BPB
    return


# version
__id__ = "$Id$"

# End of file 
