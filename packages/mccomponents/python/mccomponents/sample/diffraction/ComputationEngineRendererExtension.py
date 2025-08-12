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

import os, numpy as np

nsampling = 100

class ComputationEngineRendererExtension:


    def onSingleCrystalDiffractionKernel(self, kernel):
        '''handler to create c++ instance of a single crystal diffraction kernel.
        '''
        # kernel object is created in the parser components
        # get unit cell
        scatterer = kernel.scatterer_origin
        try:
            unitcell = scatterer.phase.unitcell
        except AttributeError as err:
            raise RuntimeError("Cannot obtain unitcell from scatterer %s, %s" % (
                scatterer.__class__.__name__, scatterer.name ))
        assert np.allclose(unitcell.lattice.base, kernel.basis_vectors, atol=1e-3), (
            "basis vectors mismatch. From crystal data: {}; from diffraction data: {}".format(
                unitcell.lattice.base, kernel.basis_vectors))
        # hkllist is a list of mccomponents.sample.diffraction.singlecrystal.HKL instance
        # need to convert to a list of h,k,l,F2
        hkllist2 = []
        for hkl in kernel.hkllist:
            h,k,l = hkl.hkl
            F2 = hkl.F_squared
            hkllist2.append((h,k,l,F2))
            continue
        from sampleassembly import cross_sections
        abs_xs, inc_xs, coh_xs = cross_sections( scatterer, include_density=False)
        abs_xs /= units.area.barn
        mosaic = kernel.mosaic / units.angle.radian
        delta_d_d = kernel.Dd_over_d
        return self.factory.singlecrystaldiffractionkernel(
            kernel.basis_vectors, hkllist2, mosaic, delta_d_d, abs_xs)

    def onSimplePowderDiffractionKernel(self, kernel):
        '''handler to create c++ instance of a simple powder diffraction kernel.
        '''
        # get unit cell
        # scatterer = kernel.scatterer_origin
        # try: unitcell = scatterer.phase.unitcell
        # except AttributeError, err:
        #    raise "Cannot obtain unitcell from scatterer %s, %s" % (
        #        scatterer.__class__.__name__, scatterer.name )
        
        #
        from .SimplePowderDiffractionKernel import Data
        data = Data()
        
        #
        data.Dd_over_d = kernel.Dd_over_d
        #
        #data.unitcell_volume = unitcell.getVolume()
        data.unitcell_volume = kernel.unitcell_volume
        # !!!!!
        # number_of_atoms is not really used in the kernel implementation
        # needs double check
        data.number_of_atoms = 0 #unitcell.getNumAtoms()
        # !!!!!
        # atomic_weight is not really used in the kernel implementation
        # needs double check
        data.atomic_weight = 0
        # !!!!!
        # density is not really used in the kernel implementation
        # needs double check
        data.density = 0
        # !!!!!
        # debye waller factor probably should be computed by default
        # needs improvement
        data.DebyeWaller_factor = kernel.DebyeWaller_factor
        
        # This was the old implementation.
        # Problem is that the data in the diffraction peaks file (such as laz)
        # may not match the unit cell choice in the "scatterer" data object,
        # which usually comes from an xyz file.
        # from sampleassembly import cross_sections
        # abs, inc, coh = cross_sections( scatterer, include_density=False)
        #
        # The new implementation here assumes the kernel specification
        # provides these information
        xs = kernel.cross_sections
        abs, inc, coh = xs.abs, xs.inc, xs.coh
        data.absorption_cross_section = abs # /units.area.barn
        data.incoherent_cross_section = inc # /units.area.barn
        data.coherent_cross_section = coh # /units.area.barn
        
        # 
        data.peaks = kernel.peaks
        
        return self.factory.simplepowderdiffractionkernel(data)


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


from . import units


# version
__id__ = "$Id$"

# End of file 
