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


    def onPhonon_IncoherentElastic_Kernel(self, kernel):
        '''handler to create c++ instance of phonon incoherent elastic
        scattering kernel.
        '''
        # get unit cell
        scatterer = kernel.scatterer_origin
        try: unitcell = scatterer.phase.unitcell
        except AttributeError, err:
            raise "Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name )

        # additional kernel parameters
        AA= units.length.angstrom
        dw_core = kernel.dw_core / AA**2
        
        return self.factory.phonon_incoherentelastic_kernel(
            unitcell, dw_core,
            )


    def onPhonon_IncoherentInelastic_Kernel(self, kernel):
        '''handler to create c++ instance of phonon incoherent inelastic
        scattering kernel.
        '''
        # get unit cell
        scatterer = kernel.scatterer_origin
        try: unitcell = scatterer.phase.unitcell
        except AttributeError, err:
            raise "Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name )

        # environment temperature
        temperature = getTemperature(scatterer)
        
        # total mass of unitcell. for DW calculator. this might be reimplemented later.
        # mass = sum( [ site.getAtom().mass for site in unitcell ] )
        mass = sum( [ atom.mass for atom in unitcell ] )
        # currently we need dos to calculate DW
        try:
            dos = kernel.dos
        except AttributeError:
            raise NotImplementedError, "Should implement a way to extract dos"
        # c object of dos
        cdos = dos.identify(self)
        # c object of DW calculator
        nsampling = 100
        cdw_calculator = self.factory.dwfromDOS(
            cdos, mass, temperature, nsampling )

        # additional kernel parameters
        
        return self.factory.phonon_incoherentinelastic_kernel(
            unitcell, cdos, cdw_calculator, temperature)


    def onPhonon_CoherentInelastic_PolyXtal_Kernel(self, kernel):
        '''handler to create c++ instance of phonon coherent inelastic polyxtal
        scattering kernel.
        '''
        # scatterer
        scatterer = kernel.scatterer_origin

        # temperature
        temperature = getTemperature(scatterer)
        
        # get unit cell
        try: unitcell = scatterer.phase.unitcell
        except AttributeError, err:
            raise "Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name )

        # total mass of unitcell. for DW calculator. this might be reimplemented later.
        # mass = sum( [ site.getAtom().mass for site in unitcell ] )
        mass = sum( [ atom.mass for atom in unitcell ] )
        # currently we need dos to calculate DW
        try:
            dos = kernel.dispersion.dos
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

        meV= units.energy.meV
        angstrom = units.length.angstrom
        Ei = Ei/meV
        max_omega = max_omega/meV
        max_Q = max_Q * angstrom

        seed = kernel.seed
        
        return self.factory.phonon_coherentinelastic_polyxtal_kernel(
            cdispersion, cdw_calculator,
            unitcell, 
            temperature, Ei,  max_omega, max_Q,
            nMCsteps_to_calc_RARV,
            seed)


    def onPhonon_CoherentInelastic_SingleXtal_Kernel(self, kernel):
        '''handler to create c++ instance of phonon coherent inelastic single crystal scattering kernel.
        '''
        # get unit cell
        scatterer = kernel.scatterer_origin
        try: unitcell = scatterer.phase.unitcell
        except AttributeError, err:
            raise "Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name )

        # environment temperature
        temperature = getTemperature(scatterer)

        # total mass of unitcell. for DW calculator. this might be reimplemented later.
        # mass = sum( [ site.getAtom().mass for site in unitcell ] )
        mass = sum( [ atom.mass for atom in unitcell ] )
        # currently we need dos to calculate DW
        try:
            dos = kernel.dispersion.dos
        except AttributeError:
            raise NotImplementedError, "Should implement a way to extract dos from dispersion"
        # c object of dos
        cdos = self.factory.dos_fromhistogram( dos )
        # c object of DW calculator
        cdw_calculator = self.factory.dwfromDOS(
            cdos, mass, temperature, nsampling )

        # additional kernel parameters
        # Ei = kernel.Ei
        
        #
        cdispersion = kernel.dispersion.identify(self)
        
        # meV= units.energy.meV
        # Ei = Ei/meV
        
        return self.factory.phonon_coherentinelastic_singlextal_kernel(
            cdispersion, cdw_calculator,
            unitcell, 
            temperature,
            )


    def onLinearlyInterpolatedDispersionOnGrid(self, dispersion):
        natoms = dispersion.nAtoms
        Qaxes = dispersion.Qaxes
        eps_npyarr = dispersion.eps_npyarr
        E_npyarr = dispersion.E_npyarr
        return self.factory.linearlyinterpolateddispersion(
            natoms, Qaxes, eps_npyarr, E_npyarr )


    def onPeriodicDispersion(self, dispersion):
        core = dispersion.dispersion
        ccore = core.identify(self)
        rcell = dispersion.reciprocalcell
        return self.factory.periodicdispersion( ccore, rcell )


    def onLinearlyInterpolatedDOS(self, dos):
        doshist = dos.doshist
        return self.factory.dos_fromhistogram(doshist)
    

    pass # end of ComputationEngineRendererExtension



def getTemperature(scatterer):
    # environment temperature
    # desired implementation:
    # environment = scatterer.environment
    # temperature = environment.temperature

    # sample assembly
    # XXX: probably should be a loop until it gets to the root
    sampleassembly = scatterer.parent()
    # check sampleassembly
    from sampleassembly.elements.SampleAssembly import SampleAssembly
    if sampleassembly is not None and not isinstance(sampleassembly, SampleAssembly):
        raise RuntimeError("%s is not a sampleassembly" % (sampleassembly,))
    # get sample environment if sampleassembly exists
    environ = sampleassembly.getEnvironment() \
              if sampleassembly is not None \
              else None

    # get temperature if sample environment exists
    from . import units
    temperature = environ.temperature()/units.temperature.K \
                  if environ is not None \
                  else 300
    return temperature


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
