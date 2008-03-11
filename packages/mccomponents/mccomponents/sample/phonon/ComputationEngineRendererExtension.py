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


nsampling = 100

class ComputationEngineRendererExtension:


    def onPhonon_CoherentInelastic_PolyXtal_Kernel(self, kernel):
        '''handler to create c++ instance of phonon coherent inelastic polyxtal
        scattering kernel.
        '''
        # get unit cell
        scatterer = kernel.scatterer_origin
        try: unitcell = scatterer.phase.unitcell
        except AttributeError, err:
            raise "Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name )

        # environment temperature
        environment = scatterer.environment
        temperature = environment.temperature

        # total mass of unitcell. for DW calculator. this might be reimplemented later.
        mass = sum( [ site.getAtom().mass for site in unitcell ] )
        # currently we need dos to calculate DW
        try:
            dos = kernel.dos
        except AttributeError:
            raise NotImplementedError, "Should implement a way to extract dos from dispersion"
        # c object of dos
        cdos = self.factory.dos_fromhistogram( dos )
        # c object of DW calculator
        cdw_calculator = self.factory.dwfromDOS(
            cdos, mass, temperature, nsampling )

        # additional kernel parameters
        Ei = kernel.Ei
        max_omega = kernel.max_omega
        max_Q = kernel.max_Q
        nMCsteps_to_calc_RARV = kernel.nMCsteps_to_calc_RARV
        cdispersion = kernel.dispersion.identify(self)
        
        return self.factory.phonon_coherentinelastic_polyxtal_kernel(
            cdispersion, cdw_calctor,
            unitcell, 
            temperature, Ei,  max_omega, max_Q,
            nMCsteps_to_calc_RARV)


    def onLinearlyInterpolatedDispersionOnGrid(self, dispersion):
        natoms = dispersion.nAtoms
        Qaxes = dispersion.Qaxes
        eps_npyarr = dispersion.eps_npyarr
        E_npyarr = dispersion.E_npyarr
        return self.factory.linearlyinterpolateddispersion(
            natoms, Qaxes, eps_npyarr, E_npyarr )
    

    pass # end of ComputationEngineRendererExtension



def register( type, renderer_handler_method, override = False ):
    '''register computing engine constructor method for a new type'''

    Renderer = ComputationEngineRendererExtension
    global _registry

    name = type.__name__
    methodname = 'on%s' % name
    if hasattr(Renderer, methodname):
        if not override:
            raise ValueError , "Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                type, methodname, _registry[name] )
        pass
    
    setattr( Renderer, methodname, renderer_handler_method )

    _registry[ name ] = type
    return
_registry = {}



from mccomponents.homogeneous_scatterer import registerRendererExtension
registerRendererExtension( ComputationEngineRendererExtension )


import units


# version
__id__ = "$Id$"

# End of file 
