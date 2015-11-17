#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class SimplePowderDiffractionKernel(Kernel):

    '''a simple kernel for powder diffraction
    '''

    def __init__(self, Dd_over_d, DebyeWaller_factor, peaks, unitcell_volume=None, cross_sections=None):
        '''new SimplePowderDiffractionKernel
  Inputs:
    Dd_over_d: relative line width Delta_d/d
    DebyeWaller_factor: Debye-Waller factor
    peaks: data of all powder diffraction peaks. a peak should be an instance of Peak
    unitcell_volume: unit is \AA^3
    cross_sections: data structure containing attributes coh, inc, and abs. total cross sections of a unit cell
    '''
        self.Dd_over_d = Dd_over_d
        self.DebyeWaller_factor = DebyeWaller_factor
        self.peaks = peaks
        self.unitcell_volume = unitcell_volume
        self.cross_sections = cross_sections
        return
        
    def identify(self, visitor): 
        return visitor.onSimplePowderDiffractionKernel(self)
    
    pass



class Data:

    peaks = [] # peaks should be a list of instances of Peak
    Dd_over_d = 0
    DebyeWaller_factor = 0
    density = 0
    atomic_weight = 0
    unitcell_volume = 0
    number_of_atoms = 0
    absorption_cross_section = 0
    incoherent_cross_section = 0


from .powder import Peak


# version
__id__ = "$Id$"

# End of file 
