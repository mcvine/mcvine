#!/usr/bin/env python
#
#


import journal
import periodictable


nsampling = 100

from mcni.components.ParallelComponent import MPI

class ComputationEngineRendererExtension:


    def onSANSSpheresKernel(self, kernel):
        '''handler to create c++ instance of SANSSpheresKernel
        '''
        ul = units.length
        abs_coeff = kernel.abs_coeff
        if abs_coeff is None:
            from sampleassembly import compute_absorption_and_scattering_coeffs
            origin = kernel.scatterer_origin
            abs_coeff, inc, coh = compute_absorption_and_scattering_coeffs(origin)
        abs_coeff = self._unitsRemover.remove_unit( abs_coeff, 1./ul.m )
        R = self._unitsRemover.remove_unit( kernel.R, ul.angstrom )
        phi = kernel.phi
        delta_rho = self._unitsRemover.remove_unit( kernel.delta_rho, 1e-15*ul.m/ul.angstrom**3 )
        max_angle = self._unitsRemover.remove_unit( kernel.max_angle, units.angle.deg )
        # print("max_angle=", max_angle)
        return self.factory.sans_spheres_kernel(abs_coeff, R, phi, delta_rho, max_angle)

    pass # end of ComputationEngineRendererExtension


def register( type, renderer_handler_method, override = False ):
    '''register computing engine constructor method for a new type'''

    Renderer = ComputationEngineRendererExtension
    global _registry

    name = type.__name__
    methodname = 'on%s' % name
    if hasattr(Renderer, methodname):
        if not override:
            raise ValueError("Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                type, methodname, _registry[name] ))
        pass
    setattr( Renderer, methodname, renderer_handler_method )

    _registry[ name ] = type
    return
_registry = {}

from mccomponents.homogeneous_scatterer import registerRendererExtension
registerRendererExtension( ComputationEngineRendererExtension )

from mcni import units

# End of file 
