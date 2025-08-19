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


import periodictable
import logging
logger = logging.getLogger("MCVine")


nsampling = 100

from mcni.components.ParallelComponent import MPI

class ComputationEngineRendererExtension:

    def onPhonon_IncoherentElastic_Kernel(self, kernel):
        '''handler to create c++ instance of phonon incoherent elastic
        scattering kernel.
        '''
        # get unit cell
        scatterer = kernel.scatterer_origin
        try: unitcell = scatterer.phase.unitcell
        except AttributeError as err:
            raise "Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name )

        # additional kernel parameters
        AA= units.angstrom
        dw_core = kernel.dw_core / AA**2
        
        # additional kernel parameters
        scattering_xs = kernel.scattering_xs/units.barn \
            if kernel.scattering_xs else 0.
        absorption_xs = kernel.absorption_xs/units.barn \
            if kernel.absorption_xs else 0.
        
        return self.factory.phonon_incoherentelastic_kernel(
            unitcell, dw_core,
            scattering_xs = scattering_xs, 
            absorption_xs = absorption_xs,
            )


    def onPhonon_IncoherentInelastic_Kernel(self, kernel):
        '''handler to create c++ instance of phonon incoherent inelastic
        scattering kernel.
        '''
        # get unit cell
        scatterer = kernel.scatterer_origin
        try: unitcell = scatterer.phase.unitcell
        except AttributeError as err:
            raise "Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name )

        # environment temperature
        temperature = getTemperature(scatterer)
        
        # total mass of unitcell. for DW calculator. this might be reimplemented later.
        # mass = sum( [ site.getAtom().mass for site in unitcell ] )
        average_mass = kernel.average_mass
        if not average_mass:
            mass = sum( [ getattr(periodictable, atom.element).mass for atom in unitcell ] )
            average_mass = mass/len(unitcell)
        else:
            average_mass = average_mass/units.u
            
        # currently we need dos to calculate DW
        try:
            dos = kernel.dos
        except AttributeError:
            raise NotImplementedError("Should implement a way to extract dos")
        # c object of dos
        cdos = dos.identify(self)
        # c object of DW calculator
        nsampling = 100
        cdw_calculator = self.factory.dwfromDOS(
            cdos, average_mass, temperature, nsampling )
        
        # additional kernel parameters
        scattering_xs = kernel.scattering_xs/units.barn \
            if kernel.scattering_xs else 0.
        absorption_xs = kernel.absorption_xs/units.barn \
            if kernel.absorption_xs else 0.

        return self.factory.phonon_incoherentinelastic_kernel(
            unitcell, cdos, cdw_calculator, temperature,
            ave_mass = average_mass, 
            scattering_xs = scattering_xs, absorption_xs = absorption_xs)


    def onPhonon_IncoherentInelastic_EnergyFocusing_Kernel(self, kernel):
        '''handler to create c++ instance of phonon incoherent inelastic
        scattering kernel with energy focusing.
        '''
        # get unit cell
        scatterer = kernel.scatterer_origin
        try: unitcell = scatterer.phase.unitcell
        except AttributeError as err:
            raise "Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name )

        # environment temperature
        temperature = getTemperature(scatterer)
        
        # total mass of unitcell. for DW calculator. this might be reimplemented later.
        # mass = sum( [ site.getAtom().mass for site in unitcell ] )
        average_mass = kernel.average_mass
        if not average_mass:
            mass = sum( [ getattr(periodictable, atom.element).mass for atom in unitcell ] )
            average_mass = mass/len(unitcell)
        else:
            average_mass = average_mass/units.u
            
        # currently we need dos to calculate DW
        try:
            dos = kernel.dos
        except AttributeError:
            raise NotImplementedError("Should implement a way to extract dos")
        # c object of dos
        cdos = dos.identify(self)
        # c object of DW calculator
        nsampling = 100
        cdw_calculator = self.factory.dwfromDOS(
            cdos, average_mass, temperature, nsampling )
        
        # additional kernel parameters
        scattering_xs = kernel.scattering_xs/units.barn \
            if kernel.scattering_xs else 0.
        absorption_xs = kernel.absorption_xs/units.barn \
            if kernel.absorption_xs else 0.

        # focusing parameters
        Ef, dEf = kernel.Ef/units.meV, kernel.dEf/units.meV

        return self.factory.phonon_incoherentinelastic_energyfocusing_kernel(
            unitcell, Ef, dEf, cdos, cdw_calculator, temperature,
            ave_mass = average_mass, 
            scattering_xs = scattering_xs, absorption_xs = absorption_xs)


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
        except AttributeError as err:
            raise "Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name )

        # total mass of unitcell. for DW calculator. this might be reimplemented later.
        # mass = sum( [ site.getAtom().mass for site in unitcell ] )
        mass = sum( [ getattr(periodictable, atom.element).mass for atom in unitcell ] ) / len(unitcell)
        # currently we need dos to calculate DW
        try:
            dos = kernel.dispersion.dos
        except AttributeError:
            raise NotImplementedError("Should implement a way to extract dos from dispersion")
        # c object of dos
        cdos = self.factory.dos_fromhistogram( dos )
        # c object of DW calculator
        cdw_calculator = self.factory.dwfromDOS(
            cdos, mass, temperature, nsampling )

        # additional kernel parameters
        # Ei = kernel.Ei
        max_omega = kernel.max_omega
        # max_Q = kernel.max_Q
        # nMCsteps_to_calc_RARV = kernel.nMCsteps_to_calc_RARV
        cdispersion = kernel.dispersion.identify(self)

        meV= units.meV
        angstrom = units.angstrom
        # Ei = Ei/meV
        max_omega = max_omega/meV
        # max_Q = max_Q * angstrom
        
        # seed = kernel.seed
        
        return self.factory.phonon_coherentinelastic_polyxtal_kernel(
            cdispersion, cdw_calculator,
            unitcell, 
            temperature, max_omega,
            # Ei,  max_omega, max_Q,
            # nMCsteps_to_calc_RARV,
            # seed)
            )

    def onPhonon_CoherentInelastic_SingleXtal_Kernel(self, kernel):
        '''handler to create c++ instance of phonon coherent inelastic single crystal scattering kernel.
        '''
        # get unit cell
        scatterer = kernel.scatterer_origin
        try: unitcell = scatterer.phase.unitcell
        except AttributeError as err:
            raise "Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name )

        # environment temperature
        temperature = getTemperature(scatterer)

        # total mass of unitcell. for DW calculator. this might be reimplemented later.
        # mass = sum( [ site.getAtom().mass for site in unitcell ] )
        mass = sum( [ getattr(periodictable, atom.element).mass for atom in unitcell ] ) / len(unitcell)
        # currently we need dos to calculate DW
        try:
            dos = kernel.dispersion.dos
        except AttributeError:
            raise NotImplementedError("Should implement a way to extract dos from dispersion")
        # c object of dos
        cdos = self.factory.dos_fromhistogram( dos )
        # c object of DW calculator
        cdw_calculator = self.factory.dwfromDOS(
            cdos, mass, temperature, nsampling )

        # additional kernel parameters
        # Ei = kernel.Ei
        
        #
        cdispersion = kernel.dispersion.identify(self)
        
        # meV= units.meV
        # Ei = Ei/meV
        
        return self.factory.phonon_coherentinelastic_singlextal_kernel(
            cdispersion, cdw_calculator,
            unitcell, 
            temperature,
            )


    def onMultiPhonon_Kernel(self, kernel):
        '''handler to create c++ instance of multiphonon
        scattering kernel.
        It actually computes a S(Q,E) histogram for the multiphonon
        scattering, and then use SQEKernel plus GridSQE to do the job.
        '''
        # scatterer
        scatterer = kernel.scatterer_origin
        
        # environment temperature
        temperature = getTemperature(scatterer)
        
        # phonon dos
        try:
            dos = kernel.dos
        except AttributeError:
            raise NotImplementedError("Should implement a way to extract dos")

        dos = dos.doshist
        assert dos.__class__.__name__ == 'Histogram', \
            "%s is not a histogram" % (dos,)
        
        # get unit cell
        try: unitcell = scatterer.phase.unitcell
        except AttributeError as err:
            raise "Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name )

        # total mass of unitcell. for DW calculator. this might be reimplemented later.
        # ???
        average_mass = kernel.average_mass
        if not average_mass:
            mass = sum( [ getattr(periodictable, atom.element).mass for atom in unitcell ] )
            average_mass = mass/len(unitcell)
        else:
            average_mass = average_mass/units.u
            
        # Qmax
        Qmax = kernel.Qmax
        if Qmax:
            Qmax = Qmax * units.angstrom
        # dQ
        dQ = kernel.dQ
        if dQ:
            dQ = dQ * units.angstrom
        # Emax
        Emax = kernel.Emax
        if Emax:
            Emax = Emax / units.meV
        
        # sqe
        mpi = MPI()
        if not mpi.parallel or mpi.rank == 0:
            from .multiphonon import sqe
            q,e,s = sqe(
                dos.energy, dos.I, 
                Qmax=Qmax, dQ=dQ,
                T = temperature,
                M = average_mass, N = kernel.Nmax,
            )
            if mpi.parallel:
                channel = mpi.getUniqueChannel()
                for peer in range(1, mpi.size):
                    mpi.send((q,e,s), peer, channel)
                    continue
        else:
            channel = mpi.getUniqueChannel()
            q,e,s = mpi.receive(0, channel)
        
        import histogram as H, histogram.hdf as hh
        sqehist = H.histogram(
            'S',
            [('Q', q, 'angstrom**-1'),
             ('energy', e, 'meV')],
            s)
        # usually only a subset of sqe is necessary 
        if Emax:
            sqehist = sqehist[(), (None, Emax)].copy()
        hh.dump(sqehist, 'mp-sqe-%d.h5' % mpi.rank)
        logger.debug("computed multiphonon sqe")
        
        from mccomponents import sample
        # grid sqe
        gsqe = sample.gridsqe(sqehist)
        # q and e range
        qrange = q[0]/units.angstrom, q[-1]/units.angstrom
        erange = e[0]*units.meV, sqehist.energy[-1]*units.meV
        # kernel
        sqekernel = sample.sqekernel(
            # XXX: we may want to support more options
            # XXX: like absorption_cross_section and scattering_cross_section
            # XXX: or absorption_coefficient ...
            SQE = gsqe,
            Qrange = qrange, Erange = erange,
            absorption_cross_section = kernel.absorption_xs,
            scattering_cross_section = kernel.scattering_xs,
            )
        sqekernel.scatterer_origin = scatterer
        # 
        return sqekernel.identify(self)


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
    temperature = environ.temperature()/units.K \
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


from mcvine import units


# version
__id__ = "$Id$"

# End of file 
